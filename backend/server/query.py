from socket import timeout
from sqlite3 import connect
import pandas as pd
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch

import time 

EMBEDDER = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def embed_wrapper(ls):
    """
    Helper function which simplifies the embedding call and helps lading data into elastic easier
    """
    tic = time.perf_counter()
    # bert_embedder = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
    bert_embedder = EMBEDDER

    toc = time.perf_counter()
    
    print(toc-tic)
    results=bert_embedder.encode(ls, convert_to_tensor=True)
    results = [r.tolist() for r in results]
    return results

def search(es,query, field, type='match', index_name=None, embedder=None, size=1000):
    """
    Search elastic
    Args:
        query (string) search query
        field (string) field to search
        type (string) type of search, takes: match, term, fuzzy, wildcard (requires "*" in query), dense (semantic search, requires embedder, index needs to be indexed with embeddings, assumes embedding field is named {field}_embedding)
        index_name (string, optional) name of index, defaults to index name defined when initiating the class
        embedder (function) embedder function with expected call embedded(list of strings to embed)
        size (int, optional) number of results to retrieve, defaults to 3, max 10k, can be relaxed with elastic config
    Returns:
        DataFrame with results and search score
    """
    res=[]

    if not index_name:
        if index_name:
            index_name=index_name
        else:
            raise ValueError('index_name not provided')
    if type=='dense':
        if not embedder:
            raise ValueError('Dense search requires embedder')
        
        query_vector = embedder([query])[0]

        script_query = {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": f"cosineSimilarity(params.query_vector, '{field}_embedding') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        }

        # print(query_vector)
        # print(script_query)
        # print(field)
        res = es.search(index=index_name,body={
                "size": size,
                "query": script_query,
                "_source": {"excludes": [f'{field}_embedding']}
            }
        )


    else:
        res=es.search(index=index_name, body={'query':{type:{field:query}}, "_source": {"excludes": [f'{field}_embedding']}},size=size)
    search_raw_result=res
    hits=res['hits']['hits']
    if len(hits)>0:
        keys=list(hits[0]['_source'].keys())

        out=[[h['_score']]+[h['_source'][k] for k in keys] for h in hits]

        df=pd.DataFrame(out,columns=['_score']+keys)
    else:
        df=pd.DataFrame([])
    search_df_result=df
    # logger.debug(f'Search {type.upper()} {query} in {index_name}.{field} returned {len(df)} results of {size} requested')
    return df
