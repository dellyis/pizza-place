from pydantic import BaseModel


class Upgrades(BaseModel):
    extra_cheese: int = 0
    speedy_delivery: int = 0
    mighty_meat: int = 0
    supreme_slice: int = 0
    cheesy_crust: int = 0
    pepperoni_power: int = 0
    mega_meal: int = 0


class Ingredients(BaseModel):
    anchovy: bool = False
    avocado: bool = False
    cheese: bool = True
    cucumber: bool = False
    grass: bool = False
    mango: bool = False
    mushroom: bool = False
    olives: bool = False
    pepper: bool = False
    pineapple: bool = False
    sausage: bool = False
    tomato: bool = False
    tomato_sauce: bool = True


class Data(BaseModel):
    money: int = 0
    day: int = 1
    upgrades: Upgrades = {}
    ingredients: Ingredients = {}
