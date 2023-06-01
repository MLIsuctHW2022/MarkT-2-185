import pickle
from typing import List

import pandas as pd
from sklearn.pipeline import Pipeline

from .data_model import DataRow


class PredictionModel:
    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file, "rb") as f:
            self.model: Pipeline = pickle.load(f)

    def prediction(self, data: List[DataRow]) -> List[str]:
        return self.model.predict(
            pd.DataFrame(data=[pd.Series(x) for x in data])
        )
