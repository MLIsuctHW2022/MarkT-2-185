import random
import time
import uuid

from kafka import KafkaProducer

from src.constants import KAFKA_API_VERSION, KAFKA_SERVERS, KAFKA_TOPIC_DATA
from src.data_model import DataRow


def rand_float(s: float, e: float) -> float:
    return s + (e - s) * random.random()


if __name__ == "__main__":
    time.sleep(20)

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        api_version=KAFKA_API_VERSION,
        key_serializer=lambda x: str(x).encode("utf8"),
        value_serializer=lambda x: x.json().encode("utf8")
    )

    while True:
        producer.send(
            topic=KAFKA_TOPIC_DATA,
            key=uuid.uuid4(),
            value=DataRow(
                ph=rand_float(3, 9.5),
                temprature=random.randint(34, 90),
                taste=random.randint(0, 1),
                odor=random.randint(0, 1),
                fat=random.randint(0, 1),
                turbidity=random.randint(0, 1),
                colour=random.randint(240, 255)
            )
        )

        time.sleep(3)
