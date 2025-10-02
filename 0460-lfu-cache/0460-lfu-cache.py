class LFUCache:
    # freq: init 1 (both get put)
    # 1) valMap --> mapping key and val {key: [val, freq]}
    # 2) freqMap --> freq: OrderedDict{key:True}
    # {1: {key1: true, key2: true ...},
    #  2: {key3: true, key4: true ...},..}

    # touch: update Valmap's freq, 
    # update freqmap ->> 1) find freq using key in valMap 2) pop in freqMap, update freq (put)
    # minF = 0 

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minF = 0
        self.valMap = collections.defaultdict(list) # key: [val, freq]
        self.freMap = collections.defaultdict(collections.OrderedDict) # freq: {key:dummy(bool)}

    def touch(self, key):
        # touch: update Valmap's freq, 
        # update freqmap ->> 1) find freq using key in valMap 2) pop in freqMap, update freq (put)
        _, freq = self.valMap[key]
        self.valMap[key][1] += 1

        self.freMap[freq].pop(key)
        self.freMap[freq+1][key] = True

        if len(self.freMap[self.minF]) == 0:
            self.minF += 1

    def get(self, key: int) -> int:
        # retrun val if key existed
        if key not in self.valMap:
            return -1
        self.touch(key)
        return self.valMap[key][0] # val

    def put(self, key: int, value: int) -> None:
        # if key existed: update
        # otherwise: LRU among LFU / add, 
        if key in self.valMap:
            self.valMap[key][0] = value
            self.touch(key) 
            return
        
        if len(self.valMap) == self.cap:
            # delete LRU among LFU
            LRU, _ = self.freMap[self.minF].popitem(last=False)
            self.valMap.pop(LRU)
        
        self.valMap[key] = [value, 1]
        self.minF = 1
        self.freMap[1][key] = True


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)