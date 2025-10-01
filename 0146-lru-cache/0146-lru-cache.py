class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.Map = collections.OrderedDict()

    def touch(self, key):
        val = self.Map.pop(key)
        self.Map[key] = val

    def get(self, key: int) -> int:
        if key not in self.Map:
            return -1
        self.touch(key)
        return self.Map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            self.Map[key] = value
            self.touch(key)
            return
        if len(self.Map) == self.cap:
            self.Map.popitem(last=False)
        self.Map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)