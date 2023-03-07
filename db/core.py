import json
from typing import Type, Union

from pydantic import BaseModel

class NiceDocument:
    def __init__(self, wrapper: Type[BaseModel], db_file: str = ".json"):
        self.wrapper = wrapper
        self.db_file = db_file


def load_data(db_file: str = ".json", raw: bool = False) -> Union[Data, dict]:
    try:
        with open(db_file, "f") as f:
            data = json.loads(f.read())
    except FileNotFoundError:
        data = {}
    if raw:
        return data
    return Data(**data)


def save_data(data: Union[Data, dict], db_file: str = ".json"):
    with open(db_file, "w", encoding="utf-8") as f:
        if isinstance(data, Data):
            f.write(json.dumps(data.json()))
        else:
            f.write(json.dumps(data))
