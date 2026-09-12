class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.history = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            if key not in self.history:
                self.history.append(key)
                return self.cache[key]
            else:
                self.history.pop(self.history.index(key))
                self.history.append(key)
                return self.cache[key]
            

    def put(self, key: int, value: int) -> None:
        cache_len = len(self.cache)
        if key in self.cache: # update key
            self.cache[key] = value

            self.history.pop(self.history.index(key))
            self.history.append(key)
        else: # add new key
            if cache_len == self.capacity: 
                lru = self.history.pop(0)
                self.cache.pop(lru)

            self.cache[key] = value
            self.history.append(key)
            

        
