#!/usr/bin/env python3
import os

from kafka.config import config
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer

schema_registry_client = SchemaRegistryClient(
    {
        "url": config["SCHEMA_REGISTRY_URL"],
        'basic.auth.user.info': f"{config['API_key']}:{config['API_secret']}",
    }
)

subject_name = "retail_data-value"
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str
key_seriaizer = StringSerializer('utf_8')
avaro_serializer = AvroSerializer(schema_registry_client, schema_str)

# producer = SerializingProducer(
#     {
#         "bootstrap.servers": config["Bootstrap_server"],
#         "key.serializer": key_seriaizer,
#         "value.serializer": avaro_serializer,
#         "schema.registry.url": config["SCHEMA_REGISTRY_URL"],
#         'basic.auth.user.info': f"{config['API_key']}:{config['API_secret']}",
#     }
# )