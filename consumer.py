import time

from kafka import KafkaConsumer, KafkaProducer

from src.constants import (KAFKA_API_VERSION, KAFKA_SERVERS, KAFKA_TOPIC_DATA,
                           KAFKA_TOPIC_PREDIDCITONS, MODEL_NAME)
from src.data_model import DataRow, PredictionRow
from src.model import PredictionModel

if __name__ == "__main__":
    mdl = PredictionModel(MODEL_NAME)

    time.sleep(20)

    consumer = KafkaConsumer(
        KAFKA_TOPIC_DATA,
        bootstrap_servers=KAFKA_SERVERS,
        api_version=KAFKA_API_VERSION,
        group_id="predservice",
        auto_offset_reset="earliest"
    )

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        api_version=KAFKA_API_VERSION,
        key_serializer=lambda x: str(x).encode("utf8"),
        value_serializer=lambda x: x.json().encode("utf8")
    )

    for msg in consumer:
        value = DataRow.parse_raw(msg.value.decode("utf8")).dict()

        producer.send(
            topic=KAFKA_TOPIC_PREDIDCITONS,
            key=msg.key,
            value=PredictionRow(prediction=mdl.predict(value), **value)
        )
