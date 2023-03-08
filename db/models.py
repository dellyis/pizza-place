from pydantic import BaseModel


class Upgrades(BaseModel):
    extra_cheese: int = 0
    speedy_delivery: int = 0
    mighty_meat: int = 0
    supreme_slice: int = 0
    cheesy_crust: int = 0
    pepperoni_power: int = 0
    mega_meal: int = 0


class Data(BaseModel):
    money: int = 0
    day: int = 1
    upgrades: Upgrades = Upgrades()
