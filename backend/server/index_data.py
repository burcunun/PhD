from ast import parse
import certifi
import string
string.punctuation
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from pymongo import MongoClient
import os
import logging
import numpy as np
from elasticsearch import Elasticsearch
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sentence_transformers import SentenceTransformer
import tqdm
from elasticsearch import helpers
import json
from dotenv import load_dotenv

load_dotenv()
ES_USERNAME = os.getenv('ELASTIC_USERNAME')
ES_PASSWORD = os.getenv('ELASTIC_PASSWORD')
MONGO_CLOUD_ID = os.getenv('MONGO_CLOUD_ID')
ES_CLOUD_ID = os.getenv('ELASTIC_CLOUD_ID')

# Logger Configuration
logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("BERT-Embeder")

def fetch_data_database():
    """
        Fetch documents from the MongoDB database
        returns: pymongo.cursor.Cursor object

    """
    logger.info("\t[Fetching Data]")
    try:
        ca = certifi.where()
        client = MongoClient("127.0.0.1", 27017)
        db = client["Projects"]
        collection = db["Cordis"]
        retrieved = collection.find()#.limit(500)  # Remove limit for production
        logger.info("\t[Fetched Data Successfully]")
        return retrieved
    except:
        logger.error("\t[An error occured while fetching the data]")

def parse_data(data):
    """
        Creating a dataframe from retrived data
        data: pandas.dataframe object 
        returns: dataframe object
    """
    logger.info("\t[Creating Data Frame]")
    try:
        #df = pd.read_csv(data)
        #df = pd.DataFrame(list(data))
        df = pd.DataFrame(data)
        # df = df[["title", "summary"]]  # Experimental Remove for production
        logger.info("\t[Dataframe created successfully ]")
        return df
    except Exception as e:
        logger.info("\t[An error occured while creating the dataframe]")
        print(e)

def fetch_data_json():
    """
    """
    print("Opening publishes.json")
    with open("publishes.json") as json_file:
        data = json.load(json_file)
        #print(data)
        return data

def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree

def remove_stopwords(text, stopwords):
    output= [i for i in text if i not in stopwords]
    return output

def tokenization(text):
    tokens = text.split()
    return tokens

def embed_wrapper(ls):
    """
    Helper function which simplifies the embedding call and helps lading data into elastic easier
    """
    
    bert_embedder = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
    results=bert_embedder.encode(ls, convert_to_tensor=True)
    results = [r.tolist() for r in results]
    return results


def index_documents_text(es, df, index_name, index_field=None):
    """
        docs (list) list of dictionaries with keys matching index field names from index specification

    """

    # df_chunk = pd.read_csv(file_path, chunksize=10000, index_col=0)

    chunk_list = []  # append each chunk df here 
    chunk = df
    
    docs=json.loads(chunk.to_json(orient='records'))

    requests = []
    for i, doc in enumerate(docs):
        request = doc
        request["_op_type"] = "index"
        if index_field:
            request["_id"] = doc[index_field]
        request["_index"] = index_name
        requests.append(request)
        helpers.bulk(es, [request])


def index_documents(es, df, index_name, embedder, field_to_embed=None, index_field=None):
    """
        docs (list) list of dictionaries with keys matching index field names from index specification

    """

    # df_chunk = pd.read_csv(file_path, chunksize=10000, index_col=0)

    chunk_list = []  # append each chunk df here 
    chunk = df
    if embedder:
        chunk[f'{field_to_embed}_embedding']=embedder(chunk[field_to_embed].values)
    docs=json.loads(chunk.to_json(orient='records'))

    requests = []
    for i, doc in enumerate(docs):
        request = doc
        request["_op_type"] = "index"
        if index_field:
            request["_id"] = doc[index_field]
        request["_index"] = index_name
        requests.append(request)
        helpers.bulk(es, [request])


def create_index(es, index_name=None, text_fields=[], keyword_fields=[], dense_fields=[], dense_fields_dim=768, shards=3, replicas=1):

  index_spec={}

  index_spec['settings']={
      "number_of_shards": shards,
      "number_of_replicas": replicas,
  }

  index_spec['mappings']={
      "dynamic": "true",
      "_source": {
      "enabled": "true"
      },
      "properties": {},
  }
  for t in text_fields: 
    index_spec['mappings']['properties'][t]={
            "type": "text"
        }

  for k in keyword_fields: 
    index_spec['mappings']['properties'][k]={
            "type": "keyword"
        }

  for d in dense_fields: 
    index_spec['mappings']['properties'][d]={
            "type": "dense_vector",
            "dims": dense_fields_dim
        }
    
  print(f"Creating '{index_name}' index.")

  es.indices.create(index=index_name, body=index_spec)

def create_index_text(es, index_name=None, text_fields=[], keyword_fields=[], shards=3, replicas=1):
    index_spec={}

    index_spec['settings']={
        "number_of_shards": shards,
        "number_of_replicas": replicas,
    }

    index_spec['mappings']={
        "dynamic": "true",
        "_source": {
        "enabled": "true"
        },
        "properties": {},
    }
    for t in text_fields: 
        index_spec['mappings']['properties'][t]={
                "type": "text"
            }

    for k in keyword_fields: 
        index_spec['mappings']['properties'][k]={
                "type": "keyword"
            }
        
    print(f"Creating '{index_name}' index.")

    es.indices.create(index=index_name, body=index_spec)


def main():

    # Connect to ElasticSearch
    try:
        logger.error("[\tConnecting to elasticsearch...]")
        print(ES_PASSWORD)
        #es = Elasticsearch(cloud_id=ES_CLOUD_ID, basic_auth=(ES_USERNAME, ES_PASSWORD), verify_certs=True, ca_certs=os.getcwd() + "\\A2525B64D8BFD084D946539261844AC9A3F7DBDC.crt")
        es = Elasticsearch("http://localhost:9200")
        es.ping()
        logger.info("\t[Connected Successfully]")
    except:
        logger.error("\t[Failed to connect to elastic search]")
    
    # Fetch data
    #data =fetch_data_database()
    data = fetch_data_json()
    print(type(data))
    df = parse_data(data)
    #print(df)
    # +++++ Preprocess Titles +++++
    # Remove punctuation
    df['title_cleaned']= df['title'].apply(lambda x: remove_punctuation(x))
    # Lower case 
    df['title_cleaned']= df['title_cleaned'].apply(lambda x: x.lower())
    # Tokenize
    df['title_tokenized']= df['title_cleaned'].apply(lambda x: tokenization(x))
    # Removing Stopwords
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
    df['title_cleaned']= df['title_tokenized'].apply(lambda x:remove_stopwords(x, stopwords))
    # Detokenize
    titles = []
    for row in df.itertuples():
        title = TreebankWordDetokenizer().detokenize(row.title_tokenized)
        titles.append(title)

    df["title_cleaned"] = titles
    del df['title_tokenized']

    #print(df)
    # ++++ Bert Embedder ++++
    create_index(es, index_name='big_sample_text_sbert',
    text_fields=['title', 'summary', 'keywords', 'source', 'language', 'totalCost', 'ecMaxContribution', 'duration', 'title_cleaned', "endDate", "database" ],
     dense_fields=['title_cleaned_embedding'],
     dense_fields_dim=384)

    index_documents(es, df,
     index_name='big_sample_text_sbert',
     field_to_embed='title_cleaned', embedder=embed_wrapper, index_field="_id")

main()
