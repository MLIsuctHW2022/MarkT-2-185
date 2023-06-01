import os

KAFKA_SERVERS = os.getenv("KAFKA_SERVERS")
KAFKA_TOPIC_DATA = os.getenv("KAFKA_TOPIC_DATA")
KAFKA_TOPIC_PREDIDCITONS = os.getenv("KAFKA_TOPIC_PREDIDCITONS")
KAFKA_API_VERSION = (0, 10, 5)

MODEL_NAME = "model.pkl"

ALLOWED_PREDICTIONS = [
    'high',
    'medium',
    'low'
]
