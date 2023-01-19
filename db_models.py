from db_core import NiceDocument, NiceField


class Upgrades(NiceField):
    long_days: bool
    happiness: bool
animator: bool
    additional_slot: bool


class Data(NiceDocument):
    money: int
    gems: int
upgrades: Upgrades
