#import re
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#from pyspark.sql.functions import col
#from pyspark.ml import PipelineModel
#from sklearn.base import BaseEstimator

import pickle
import nltk
from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient
from pyspark.sql import SparkSession
from sklearn.base import TransformerMixin
import spacy
import numpy as np
from spacy.lang.en.stop_words import STOP_WORDS
stop_words = STOP_WORDS
import string
punctuations = string.punctuation

# Download stopwords
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


#predictors & clean text
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]

    def fit(self, X, y, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}
def clean_text(text):
    return text.strip().lower()

# Creating our tokenizer function
nlp = spacy.load('en_core_web_sm')
def spacy_tokenizer(sentence):
    mytokens = nlp(sentence)
    lemmatized_tokens = []
    for word in mytokens:
        lemma = word.lemma_
        if lemma != "-PRON-":
            lemma = lemma.lower().strip()
        else:
            lemma = word.lower_
        lemmatized_tokens.append(lemma)
    final_tokens = [word for word in lemmatized_tokens if word not in stop_words and word not in punctuations]
    return final_tokens

# Load the model
headline_model = pickle.load(open("Kafka-pyspark/headline_prediction_model.pkl", 'rb'))
title_model = pickle.load(open("Kafka-pyspark/title_prediction_model.pkl", 'rb'))

# Establish connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['bigdata_project']
collection = db['news']

# Assuming you have a SparkSession already created
spark = SparkSession.builder \
    .appName("classify news") \
    .getOrCreate()

# Kafka Consumer
consumer = KafkaConsumer(
    'numtest',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print(message)
    title = message.value['Title']
    headline = message.value['Headline']

    title = clean_text(title)
    headline = clean_text(headline)

    # print("-> tweet : ", tweet)
    # print("-> preprocessed_tweet : ", preprocessed_tweet)

    # Prediction
    X_test_tit = np.array([title], dtype=object)
    X_test_head = np.array([headline], dtype=object)

    pred_title = title_model.predict(X_test_tit)
    pred_headline = headline_model.predict(X_test_head)

    # Print prediction
    print(f"Title:{title} \n-> Sentiment:{pred_title[0, 0]}")
    print(f"Headline:{headline} \n-> Sentiment:{pred_headline[0, 0]}")


    # Prepare document to insert into MongoDB
    news_doc = {
        "title": title,
        "tit_prediction": pred_title[0, 0],
        "headline": headline,
        "head_prediction": pred_headline[0, 0]
    }

    # Insert document into MongoDB collection
    collection.insert_one(news_doc)
    print("/"*50)