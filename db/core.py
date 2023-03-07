import json
from typing import Type

from pydantic import BaseModel


class NiceDocument:
    def __init__(self, wrapper: Type[BaseModel], db_file: str = ".json"):
        self.wrapper = wrapper
        self.db_file = db_file
        self.data = None

    def __getattr__(self, attr):
        if attr in self.data.__fields__:
            return getattr(self.data, attr)
        return getattr(self, attr)

    def load(self):
        try:
            with open(self.db_file) as f:
                data = json.loads(f.read())
        except FileNotFoundError:
            data = {}
        self.data = self.wrapper(**data)

    def save(self):
        with open(self.db_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.data.json()))
