from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
from client import *
# from sentence_transformers import SentenceTransformer

load_dotenv()
ES_USERNAME = os.getenv('ELASTIC_USERNAME')
ES_PASSWORD = os.getenv('ELASTIC_PASSWORD')
IP_ADDRESS = os.getenv("IP_ADDRESS")
# EMBEDDER = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

ES = connect_es(ES_USERNAME, ES_PASSWORD)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def check():
    res = {'response': "OK"}
    return jsonify(res)

@app.route('/query/dense_vectors', methods=['POST'])
@cross_origin()
def search_dense():
    data = request.json
    res = search_dense_vectors(data['term'], ES)
    return jsonify(res)


app.run(host=IP_ADDRESS)
