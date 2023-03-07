from pydantic import BaseModel


class Upgrades(BaseModel):
    long_days: bool = False
    happiness: bool = False
    animator: bool = False


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
    gems: int = 0
    day: int = 1
    upgrades: Upgrades
    ingredients: Ingredients
