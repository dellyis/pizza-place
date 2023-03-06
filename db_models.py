from pydantic import BaseModel


class Upgrades(BaseModel):
    long_days: bool = False
    happiness: bool = False
    animator: bool = False


class Data(BaseModel):
    money: int = 0
    gems: int = 0
    upgrades: Upgrades
