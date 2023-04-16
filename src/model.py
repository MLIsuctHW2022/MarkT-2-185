import pickle

import pandas as pd
from sklearn.pipeline import Pipeline

from .data_model import DataRow


class PredictionModel:
    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file, "rb") as f:
            self.model: Pipeline = pickle.load(f)

    def predict(self, data: DataRow) -> str:
        series = pd.Series(data)
        df = pd.DataFrame(data=[series])
        prediction = self.model.predict(df)
        return prediction[0]
