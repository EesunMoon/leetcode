# get & put => counter
# LRU + LFU: [kvmap] {k: (v, f)}, [freqmap] {freq: {k:True}}
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv = {} # key:(val,freq)
        self.countMap = collections.defaultdict(OrderedDict) # freq: {k:True,..}
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        # update the freq
        self.touch(key)
        return self.kv[key][0]
    
    def touch(self, key):
        val, freq = self.kv[key]
        self.countMap[freq].pop(key)
        self.countMap[freq+1][key] = True
        self.kv[key] = [val, freq+1]
        if freq == self.minFreq and len(self.countMap[freq])==0:
            self.minFreq += 1
        
    def put(self, key: int, value: int) -> None:
        # case 1) just update the values:: update -> touch
        # case 2) add new val:: add -> touch
        ## edge case 2-1) capacity:: remove lru
        if self.cap == 0:
            return
        if key in self.kv:
            self.kv[key] = [value, self.kv[key][1]]
            self.touch(key)
            return
        
        # edge case
        if len(self.kv) == self.cap:
            lru, _ = self.countMap[self.minFreq].popitem(last=False)
            self.kv.pop(lru)
        self.kv[key] = [value, 1]
        self.minFreq = 1
        self.countMap[1][key] = True

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)