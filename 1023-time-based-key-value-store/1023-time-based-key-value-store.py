from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key: [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        # timestamp_prev <= timestamp
        cand = self.store[key]
        res = ""
        l, r = 0, len(cand)-1
        while l<=r:
            m = (l+r)//2
            if cand[m][0] == timestamp:
                return cand[m][1] # value
            elif cand[m][0] > timestamp:
                r = m - 1
            else:
                res = cand[m][1]
                l = m + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)