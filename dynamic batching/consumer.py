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
        auto_offset_reset="earliest",
        value_deserializer=lambda x: DataRow.parse_raw(x.decode('utf8'))
    )

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        api_version=KAFKA_API_VERSION,
        key_serializer=lambda x: str(x).encode("utf8"),
        value_serializer=lambda x: x.json().encode("utf8")
    )

    while True:
        received = []
        for _ in range(20):
            try:
                msg = consumer.next_v2()
                consumer.commit()
                received.append(msg)
            except StopIteration:
                break

        if len(received) > 0:
            keys = []
            for x in received:
                keys.append(x.key)

            vals = []
            for x in received:
                vals.append(x.value.dict())

            prds = mdl.prediction(vals)

            for i in range(len(keys)):
                producer.send(
                    topic=KAFKA_TOPIC_PREDIDCITONS,
                    key=keys[i],
                    value=PredictionRow(prediction=prds[i], **vals[i])
                )
