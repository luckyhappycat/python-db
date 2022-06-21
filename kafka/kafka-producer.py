import imp
import kafka
import json
import datetime
import time

producer = kafka.KafkaProducer(
    bootstrap_servers=["127.0.0.1:9092"],
    # sasl_plain_username=None,
    # sasl_plain_password=None,
)
print(producer.config)
print("producer init successfully")

for i in range(100):
    future = producer.send(
        topic="test-topic",
        value=json.dumps(
            {
                "method": "get",
                "step": "1",
                "type": "test",
                "testName": "kafka",
                "cid": "{0}".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
                "info": "demo{}".format(1)
            },
        ).encode(encoding="utf-8"),
        partition=0
    )
    record_metadata = future.get(timeout=10)
    print(record_metadata, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    time.sleep(0.5)

# producer.send(
#     topic="test-topic",
#     key="key-1",
#     value="value-1",
#     # partition=1
# )
# print("producer send successfully")
