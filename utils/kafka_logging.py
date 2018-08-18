import json
import logging
import sys

from confluent_kafka import Producer


class KafkaHandler(logging.Handler):

    def __init__(self, kafka_bootstrap_servers, kafka_topic, data_serializer_func):
        logging.Handler.__init__(self)
        self.producer = Producer({'bootstrap.servers': kafka_bootstrap_servers})
        self.kafka_topic = kafka_topic
        self.data_serializer_func = data_serializer_func

    def delivery_report(self, err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def emit(self, record):
        try:
            self.producer.poll(1.0)
            msg = self.format(record)
            self.producer.produce(self.kafka_topic, self.data_serializer_func(msg), callback=self.delivery_report)
        except Exception as e:
            print(e)
            logging.Handler.handleError(self, record)

    def close(self):
        self.producer.flush(timeout=1.0)
