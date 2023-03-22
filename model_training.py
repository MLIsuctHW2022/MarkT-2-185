import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.constants import MODEL_NAME

RANDOM_STATE = 42
TEST_SIZE = 0.2

N_ESTIMATORS = 50
MAX_FEATURES = 0.35

MODEL_TYPE = GradientBoostingClassifier(
    n_estimators=N_ESTIMATORS,
    max_features=MAX_FEATURES,
    random_state=RANDOM_STATE
)

NUMERIC_COLS = [
    "ph",
    "temprature",
    "taste",
    "odor",
    "fat",
    "turbidity",
    "colour"
]

TARGET = "grade"

print("loading")
df = pd.read_csv("milk.csv")

X = df.drop(TARGET, axis="columns")
y = df[TARGET]

print("splitting")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

preprocessor = ColumnTransformer([
    ("standard", StandardScaler(), NUMERIC_COLS),
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", MODEL_TYPE)
])

print("training")
model.fit(X_train, y_train)

print("score", model.score(X_test, y_test))

with open(MODEL_NAME, "wb") as f:
    pickle.dump(model, f)
