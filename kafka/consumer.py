#!/usr/bin/env python3
import logging
import sys
from kafka_config import config as kafka_config
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.schema_registry.avro import AvroDeserializer

def main(groupid:str):
    logging.basicConfig(level=logging.DEBUG, format='%(process)d - %(levelname)s - %(message)s')
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
            'group.id': groupid,
            'key.deserializer': key_deserializer,
            'value.deserializer': avro_deserializer,
            'auto.offset.reset':'Earliest',
        }
    )

    consumer.subscribe(["retail_data"])
    file = open('data.txt','a')
    try:
        while True:
            logging.info("Polling Msg")
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                logging.error(f"Consumer error. {msg.error()}")
                continue

            logging.info(f"Successfully consumed the message {msg.key()} - {msg.value()}")
            file.write(msg.key()+','+'\n')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        file.close()

if __name__ == "__main__":
    group_id = sys.argv[1]
    main(group_id)
