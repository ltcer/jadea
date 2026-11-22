class Cache:
    def __init__(self, limit=100):
        self.limit = limit
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        if len(self.data) >= self.limit:
            self.data.pop(next(iter(self.data)))
        self.data[key] = value
