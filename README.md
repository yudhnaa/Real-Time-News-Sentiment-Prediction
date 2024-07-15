# Real Time News Sentiment Prediction
A machine learning model and Realtime analysis

# Machine Learning Model

## Repository Structure
- **Kafka-PySpark** : this folder contains kafka provider and pyspark streaming (kafka consumer).
  **zk-single-kafka-single.yml** : Download and install Apache Kafka in docker.
-  **Machine Learning** : this folder contains the trained model with jupyter notebook and datasets.
  
## Dataset

This is a large data set of news items and their respective social feedback on multiple platforms: `Facebook`, `Google+` and `LinkedIn`. 

The collected data relates to a period of 8 months, between November 2015 and July 2016, accounting for about 100,000 news items on four different topics: `economy`, `microsoft`, `obama` and `palestine`. 

This data set is tailored for evaluative comparisons in predictive analytics tasks, although allowing for tasks in other research areas such as topic detection and tracking, sentiment analysis in short text, first story detection or news recommendation. 

The dataset contains news headlines and their respective information. They include
- Facebook news
- Google+ news
- Linkedln news

The attributes for each of the tables are : 
- **IDLink (numeric):** Unique identifier of news items
- **Title (string):** Title of the news item according to the official media sources
- **Headline (string):** Headline of the news item according to the official media sources
- **Source (string):** Original news outlet that published the news item
- **Topic (string):** Query topic used to obtain the items in the official media sources
- **Publish-Date (timestamp):** Date and time of the news items' publication
- **Sentiment-Title (numeric):** Sentiment score of the text in the news items' title
- **Sentiment-Headline (numeric):** Sentiment score of the text in the news items' headline 
- **Facebook (numeric):** Final value of the news items' popularity according to the social media source Facebook
- **Google-Plus (numeric):** Final value of the news items' popularity according to the social media source Google+
- **LinkedIn (numeric):** Final value of the news items' popularity according to the social media source LinkedIn
- **SentimentTitle:** Sentiment score of the title, Higher the score, better is the impact or +ve sentiment and vice-versa. _(Target Variable 1)_
- **SentimentHeadline:** Sentiment score of the text in the news items' headline. Higher the score, better is the impact or +ve sentiment. _(Target Variable 2)_



## Solution 1: Custom Transform pipelines with Multi-Output Regressor

A pipeline in sklearn is a set of chained algorithms to extract features, preprocess them and then train or use a machine learning algorithm. Each pipeline has a number of steps, which is defined as a list of tuples. The first element in the tuple is the name of the step in the pipeline. The second element of the tuple is the transformer. When predicting an outcome the pipeline preprocesses the data before running it through the estimator to predict the outcome.

A pipeline component is defined as a `TransformerMixin` derived class with two important methods:

`fit` - Uses the input data to train the transformer

`transform` - Takes the input features and transforms them

The `fit` method is used to train the transformer. This method is used by components such as the CountVectorizer to setup the internal mappings for words to vector elmeents. It gets both the features and the expected output.

The `transform` method only gets the features that need to be transformed. It returns the transformed features.

The final step in the pipeline is the estimator. The estimator can be a classifier, regression algorithm, a neural network or even some unsupervised algorithm.

Here I created a custom pipeline used Scikit-learn's `TransformerMixin` and used a regressor like `Random Forrest` or `XGBRegressor`

# Real-Time News Sentiment Analysis Using Kafka, Spark (MLLib & Streaming), MongoDB.
## Overview

This repository contains a Big Data project focused on real-time sentiment analysis of News data (classification of news). The project leverages various technologies to collect, process, analyze ~~, and visualize~~ sentiment data from tweets in real-time.

## Project Architecture

The project is built using the following components:

- **Apache Kafka**: Used for real-time data ingestion from News DataSet.
- **Spark Streaming**: Processes the streaming data from Kafka to perform sentiment analysis.
- **MongoDB**: Stores the processed sentiment data.


- This is the project plan :
  ![flow](https://github.com/user-attachments/assets/8c2166a7-68cc-4835-be64-0b18f2dc0cfa)
  
## Features

- **Real-time Data Ingestion**: Collects live news using Kafka from the News DataSet.
- **Stream Processing**: Utilizes Spark Streaming to process and analyze the data in real-time.
- **Sentiment Analysis**: Classifies tweets into different sentiment categories (positive, negative, neutral) using natural language processing (NLP) techniques.
- **Data Storage**: Stores the sentiment analysis results in MongoDB for persistence.

## Getting Started

### Prerequisites

To run this project, you will need the following installed on your system:

- Docker (for runing Kafka)
- Python 3.x
- Apache Kafka
- Apache Spark (PySpark for python)
- MongoDB

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yudhnaa/Real-Time-News-Predict.git
   cd Real-Time-News-Predict/Kafka-PySpark
   ```
   
2. **Installing Docker Desktop**

3. **Set up Kafka**:
   - Download and install Apache Kafka in docker using :
   ```bash
   docker-compose -f zk-single-kafka-single.yml up -d
   ```

5. **Set up MongoDB**:
   - Download and install MongoDB.
     - It is recommended to install also **MongoDBCompass** to visualize data and makes working with mongodb easier.

6. **Install Python dependencies**:
   - To install pySpark - PyMongo - ...
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

   Note : you will need MongoDB for Running the Kafka and Spark Streaming application.
   
   - **Start MongoDB**:
      - using command line :
      ```bash
      brew services start mongodb-community
      ```
      - then use **MongoDBCompass** (Recommended).

#### Running the Kafka and Spark Streaming application :

2. **Start Kafka in docker**:
   - using command line :
   ```bash
   docker exec -it <kafka-container-id> /bin/bash
   ```
   - or using docker desktop :
     ![CleanShot kafka-pyspark - App - Docker Desktop2024-07-14 at 09 26 16@2x](https://github.com/user-attachments/assets/df2e2207-6949-4cfa-90da-ac893ddbed30)


4. **Run kafka Zookeeper and a Broker**:
   - For the first time, create topic news:
   ```bash
   kafka-topics --create --topic news --bootstrap-server localhost:9092
   ```
   - Run topic news:
   ```bash
   kafka-topics --describe --topic news --bootstrap-server localhost:9092
   ```
   - Run all image 

6. **Run kafka provider app**:
   ```bash
   python producer-validation-tweets.py
   ```

7. **Run pyspark streaming (kafka consumer) app**:
   ```bash
   python consumer-pyspark.py
   ```
![CleanShot Kafka-PySpark — java ◂ python consumer-pyspark py — 80×242024-07-14 at 09 12 40@2x](https://github.com/user-attachments/assets/2ccfc4ab-44bd-4529-9fcb-0c1f3b65b786)

this is an img of the MongoDBCompass after Running the Kafka and Spark Streaming application :

![CleanShot MongoDB Compass - localhost27017bigdata_project news2024-07-14 at 09 13 27@2x](https://github.com/user-attachments/assets/7acc662b-46eb-4d12-a92b-f7b727b7a9a3)

