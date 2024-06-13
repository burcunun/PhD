import sys
from json.tool import main
from unittest import result
from elasticsearch import Elasticsearch
import json
import pandas as pd
from query import search, embed_wrapper
import time
from dotenv import load_dotenv
import os
import requests

load_dotenv()
ES_USERNAME = os.getenv('ELASTIC_USERNAME')
ES_PASSWORD = os.getenv('ELASTIC_PASSWORD')
ES_CLOUD_ID = os.getenv('ELASTIC_CLOUD_ID')

def connect_es(username, password):
    try:
        #es = Elasticsearch(cloud_id=ES_CLOUD_ID, basic_auth=(username, password), verify_certs=False)
        es = Elasticsearch("http://localhost:9200")
        print(f'Connected to elastic')
        return es
    except:
        print(f'An error occured while connecting to elastic', sys.stderr)

def tokenize_query(query):
    keywords = []
    for k in query.split():
        keywords.append(k.lower())
    return keywords

def exists_keywords(keywords, results, dense=False):
    exists = []
    keywords_exists = []
    for r in results:
        #print("r:" , r)
        keywords_that_exists = []
        for word in keywords:
            if dense:
                if word in r[3]:
                    keywords_that_exists.append(word)
            else:
                if word in r[4].lower():
                    keywords_that_exists.append(word)
                elif word in r[1].lower():
                    keywords_that_exists.append(word)
        if len(keywords_that_exists) == 0:
            exists.append(False)
            keywords_exists.append("N/A")
        else:   
            exists.append(True)
            keywords_exists.append(keywords_that_exists)
    return (exists, keywords_exists)

def getPDF(code):
    url = 'https://search.trdizin.gov.tr/pdf/view'
    myobj = {'code': code}
    x = requests.post(url, json = myobj)
    return x.text

def search_dense_vectors(query, es):
    results = []
    rank = 1
    keywords = tokenize_query(query)
    df1=search(es,query,'title_cleaned', index_name='big_sample_text_sbert',type='match',embedder=embed_wrapper)
    exists, keywords_exist = exists_keywords(keywords, df1.values)
    df1['query_exits'] = exists
    df1['query_terms'] = keywords_exist
    
    for tl in df1.values:
        """for i, tasd in enumerate(tl):
            print("a[",i,"]: ", tasd)"""

        if tl[10] == "TUBITAK":
            pdfLink = getPDF(tl[9])
        else:
            pdfLink = tl[9]
        results.append({\
            "_source": {\
            "rank": rank, \
            "score": tl[0], \
            "summary": tl[2], \
            "keywords": tl[3], \
            "language": tl[5], \
            "source": tl[4], \
            "title": tl[1], \
            "query_term_exists": tl[13], \
            "query_terms": tl[14], \
            "totalCost": tl[6], \
            "ecMaxContribution": tl[7], \
            "duration": tl[8],\
            "pdfLink": pdfLink,\
            "database": tl[10],\
            "endDate": tl[11]\
            }})
        rank+= 1
    return results
