class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        vals = self.map[key]
        l, r = 0, len(vals)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if vals[m][1] > timestamp:
                r = m-1
            else:
                res = vals[m][0]
                l = m+1
            
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)