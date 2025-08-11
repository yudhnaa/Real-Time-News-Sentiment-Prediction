# Real-Time News Sentiment Prediction

A comprehensive solution for real-time sentiment analysis on news headlines using Apache Kafka, PySpark (Spark Streaming), and MongoDB.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Dataset](#dataset)
- [Model Fine-tuning Approach](#model-fine-tuning-approach)
- [Project Architecture](#project-architecture)
- [Features](#features)
- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [Screenshots](#screenshots)

---

## Overview

This project provides a big data pipeline for real-time sentiment analysis of news articles. Data is ingested, processed in real-time, analyzed by a fine-tuned machine learning model, and results are stored for further analysis and visualization.

---

## Repository Structure

- **Kafka-PySpark/**  
  Contains Kafka producer (data provider) and PySpark streaming scripts (Kafka consumer).
  - `zk-single-kafka-single.yml` : Docker Compose file for spinning up Apache Kafka and Zookeeper.
- **Machine Learning/**  
  Includes scripts, notebooks, and datasets for model fine-tuning.

---

## Dataset

The dataset comprises about 100,000 news items with social feedback collected from **Facebook**, **Google+**, and **LinkedIn** between November 2015 and July 2016. Topics include `economy`, `microsoft`, `obama`, and `palestine`.

Each entry includes:
- News headline
- Social engagement metrics from the above platforms

This dataset supports predictive analytics, topic detection, sentiment analysis, and news recommendation tasks.

---

## Model Fine-tuning Approach

Instead of using classic ML pipelines, this project focuses on **fine-tuning** a pretrained model for sentiment analysis on news headlines.

- The **Machine Learning** folder contains scripts and notebooks for performing fine-tuning using the provided dataset.
- Fine-tuned models are loaded during real-time stream processing for accurate sentiment classification.

---

## Project Architecture

- **Apache Kafka**: Real-time ingestion of news data.
- **Spark Streaming (PySpark)**: Real-time processing and sentiment analysis using the fine-tuned model.
- **MongoDB**: Persistent storage for processed sentiment results.

---

## Features

- **Live Data Ingestion**: Streams news headlines in real-time using Kafka.
- **Stream Processing**: Spark Streaming analyzes and predicts sentiment using the fine-tuned model.
- **NLP Sentiment Classification**: Predicts sentiment scores/categories for each news item.
- **Result Storage**: Stores results in MongoDB for querying and visualization.

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) (for Kafka via Docker Compose)
- Python 3.x
- Apache Kafka
- Apache Spark (PySpark)
- MongoDB (with [MongoDB Compass](https://www.mongodb.com/products/compass) recommended for visualization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yudhnaa/Real-Time-News-Predict.git
   cd Real-Time-News-Predict/Kafka-PySpark
   ```

2. **Install Docker Desktop** (for managing containers)

3. **Set up Kafka:**
   ```bash
   docker-compose -f zk-single-kafka-single.yml up -d
   ```

4. **Set up MongoDB:**  
   Install MongoDB locally, and optionally MongoDB Compass.

5. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Project

> **Note:** MongoDB must be running before starting the Kafka and Spark Streaming applications.

1. **Start MongoDB:**
   - On macOS (with Homebrew):
     ```bash
     brew services start mongodb-community
     ```
   - Or use the MongoDB Compass GUI (recommended).

2. **Start Kafka in Docker:**
   - Open a shell inside the running Kafka container:
     ```bash
     docker exec -it <kafka-container-id> /bin/bash
     ```

3. **Create and describe Kafka topic:**
   ```bash
   kafka-topics --create --topic news --bootstrap-server localhost:9092
   kafka-topics --describe --topic news --bootstrap-server localhost:9092
   ```

4. **Run Kafka producer app:**
   ```bash
   python producer-validation-tweets.py
   ```

5. **Run PySpark streaming (Kafka consumer):**
   ```bash
   python consumer-pyspark.py
   ```

---

## Screenshots

**Kafka in Docker Desktop:**

![Kafka Docker Desktop Screenshot](https://github.com/user-attachments/assets/df2e2207-6949-4cfa-90da-ac893ddbed30)

**PySpark Consumer Running:**

![PySpark Consumer Screenshot](https://github.com/user-attachments/assets/2ccfc4ab-44bd-4529-9fcb-0c1f3b65b786)

**MongoDB Compass after Pipeline Execution:**

![MongoDB Compass Screenshot](https://github.com/user-attachments/assets/7acc662b-46eb-4d12-a92b-f7b727b7a9a3)

---

## License

This project is for research and educational purposes only.
