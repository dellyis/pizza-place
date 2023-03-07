import json
from typing import Type

from pydantic import BaseModel


class NiceDocument:
    def __init__(self, wrapper: Type[BaseModel], db_file: str = ".json"):
        self.wrapper = wrapper
        self.db_file = db_file
        self.data = None

    def load_data(self):
        try:
            with open(self.db_file, "f") as f:
                data = json.loads(f.read())
        except FileNotFoundError:
            data = {}
        self.data = self.wrapper(**data)

    def save_data(self):
        with open(self.db_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.data.json()))
