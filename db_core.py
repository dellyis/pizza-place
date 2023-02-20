import json


class NiceDocument:
    def __init__(self, db_file=".json"):
        self.db_file = db_file
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.db_file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        return data

    def _save_data(self):
        with open(self.db_file, "w") as f:
            json.dump(self.data, f)

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        self.data[key] = value
        self._save_data()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self._save_data()

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()


class NiceField:
    ...
