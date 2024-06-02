# !/usr/bin/env python
import logging
from configs.kafka_config import config as kafka_config
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.schema_registry.avro import AvroDeserializer

logging.basicConfig(level=logging.DEBUG)

schema_registry_client = SchemaRegistryClient(
    {
        "url": kafka_config["SCHEMA_REGISTRY_URL"],
        "basic.auth.user.info": f"{kafka_config['SCHEMA_REGISTRY_KEY']}:{kafka_config['BASIC_AUTH_USER_INFO']}",
    }
)

subject_name = "retail_data-value"
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str

key_deserializer = StringDeserializer("utf_8")
avro_deserializer = AvroDeserializer(schema_registry_client, schema_str)

consumer = DeserializingConsumer(
    {
        "bootstrap.servers": kafka_config["BOOTSTRAP_SERVER"],
        "security.protocol": kafka_config["security.protocol"],
        "sasl.mechanisms": kafka_config["sasl.mechanisms"],
        "sasl.username": kafka_config["API_KEY"],
        "sasl.password": kafka_config["API_SECRET"],
        'group.id':[kafka_config['GROUP_ID']],
        'key.deserializer': key_deserializer,
        'value.deserializer': avro_deserializer,
    }
)

consumer.subscribe(["retail_data"])

try:
    while True:
        logging.info("Polling Msg")
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error. {msg.error()}")
            continue

        print(f"successfully consumed the message {msg.key()} - {msg.value()}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
