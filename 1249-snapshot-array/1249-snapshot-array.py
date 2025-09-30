class SnapshotArray:

    def __init__(self, length: int):
        self.shot = [[[0,0]] for _ in range(length)] # [id, val]
        self.id = 0

    def set(self, index: int, val: int) -> None:
        if self.shot[index][-1][0] != self.id:
            self.shot[index].append([self.id, val])
        else:
            self.shot[index][-1][1] = val

    def snap(self) -> int:
        self.id += 1
        return self.id -1
        
    def get(self, index: int, snap_id: int) -> int:
        target = self.shot[index]
        l, r = 0, len(target)-1

        resId = 0
        while l<=r:
            m = (l+r)//2
            if target[m][0] == snap_id:
                return target[m][1]
            elif target[m][0] > snap_id:
                r = m - 1
            else:
                resId = max(resId, m)
                l = m + 1
        return target[resId][1]

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)