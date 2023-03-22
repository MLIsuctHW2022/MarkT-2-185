from pydantic import BaseModel, validator


class PredictionRow(BaseModel):
    ph: float
    temprature: int
    taste: int
    odor: int
    fat: int
    turbidity: int
    colour: int

    @validator("ph")
    def validate_ph(cls, v: float) -> float:
        assert 9.5 >= v >= 3, "value must be in range from 3 to 9.5"
        return v

    @validator("temprature")
    def validate_temprature(cls, v: int) -> int:
        assert 90 >= v >= 34, "value must be in range from 34 to 90"
        return v

    @validator("taste", "odor", "fat", "turbidity")
    def validate_boolean(cls, v: int) -> int:
        if v in [0, 1]:
            return v
        raise ValueError("value must be 0 or 1")

    @validator("colour")
    def validate_colour(cls, v: int) -> int:
        assert 255 >= v >= 240, "value must be in range from 240 to 255"
        return v
