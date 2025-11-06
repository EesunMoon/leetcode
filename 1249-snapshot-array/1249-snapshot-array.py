class SnapshotArray:

    def __init__(self, length: int):
        """
        row: index, store [snapID, val]
        # snapArray: array-like
        # snapTime: int - the total num of times we called snap
        """
        self.snapshot = [[[0,0]] for _ in range(length)]
        self.snapTime = 0
        

    def set(self, index: int, val: int) -> None:
        # snapArray[index] = val
        """
        if curr row list [-1] snapID modify
        else -> add
        """
        if self.snapshot[index][-1][0] == self.snapTime:
            self.snapshot[index][-1][1] = val
        else:
            self.snapshot[index].append([self.snapTime, val])

    def snap(self) -> int:
        # snapTime - 1
        self.snapTime += 1
        return self.snapTime - 1

    def get(self, index: int, snap_id: int) -> int:
        # index: [snapId, val]
        # binary searh: stored_snap_id <= snap_id
        target = self.snapshot[index]
        l, r = 0, len(target)-1
        res = 0
        while l<=r:
            m = (l+r) // 2
            if target[m][0] == snap_id:
                return target[m][1]
            elif target[m][0] > snap_id:
                r = m - 1
            else:
                res = target[m][1]
                l = m + 1
        return res


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)