import json
from typing import Union

from db_models import Data


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
