from collections import OrderedDict

class LRUCache:
    def __init__(self, size: int):
        self.cache = OrderedDict()
        self.size = size
    
    def insert(self, key: tuple[str, int], value: tuple) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.size:
            self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def contains(self, key: tuple[str, int]) -> bool:
        if key in self.cache:
            self.cache.move_to_end(key)
            return True
        else:
            return False
    
    def get(self, key: tuple[str, int]) -> any:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

