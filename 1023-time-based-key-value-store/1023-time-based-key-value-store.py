class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # key: [val, time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp]) # O(1)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        target = self.map[key]
        l, r = 0, len(target)-1
        res = ""
        while l<=r:
            m = l + (r-l)//2
            if target[m][1] == timestamp:
                return target[m][0]
            if target[m][1] > timestamp:
                r = m - 1
            else:
                res = target[m][0]
                l = m + 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)