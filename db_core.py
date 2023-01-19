import json


class NiceDocument:
    def __init__(self, file_name: str):
        with open(file_name, encoding="UTF-8") as f:
            self.data = json.loads(f.read())
        for k, v in self.data.items():
            setattr(self, k, v)


class NiceField:
    ...
