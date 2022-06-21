import kafka
import json
import datetime

producer = kafka.KafkaProducer(
    bootstrap_servers=["172.17.50.89:9092"],
    # sasl_plain_username=None,
    # sasl_plain_password=None,
)
print(producer.config)
print("producer init successfully")

future = producer.send(
    topic="test-topic",
    value=b"hello",
    # value=json.dumps(
    #     {
    #         "method": "get",
    #         "step": "1",
    #         "type": "test",
    #         "testName": "kafka",
    #         "cid": "{0}".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
    #         "info": "demo{}".format(1)
    #     },
    # ).encode(encoding="utf-8"),
    partition=1
)
# future = producer.send(
#     "test-topic",
#     b"hello",
# )
record_metadata = future.get(timeout=10)
print(record_metadata, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

# producer.send(
#     topic="test-topic",
#     key="key-1",
#     value="value-1",
#     # partition=1
# )
# print("producer send successfully")
