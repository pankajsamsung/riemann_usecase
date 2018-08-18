import logging
import json
import time
import sys


from utils.kafka_logging import KafkaHandler

print("Starting")
sys.stdout.flush()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging_handler = KafkaHandler(kafka_bootstrap_servers="kafka:9092", kafka_topic="program-logs", data_serializer_func=lambda v: json.dumps(v).encode('utf-8'))
logger.addHandler(logging_handler)

while True:
    print("Logging loop start")
    sys.stdout.flush()
    logger.info("Test my logger")
    logger.debug("Well tested log")
    print("Logging loop end")
    sys.stdout.flush()
    time.sleep(5)