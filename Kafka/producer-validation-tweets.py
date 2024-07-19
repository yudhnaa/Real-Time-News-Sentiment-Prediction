from time import sleep
import csv
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

with open('kafka/test_file.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for data in reader_obj:
        print(data)
        producer.send('numtest', value={'IDLink': data[0], 'Title': data[1], 'Headline': data[2]})
        sleep(3)