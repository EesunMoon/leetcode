class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        res = [] # stack

        # do not exceed
        for p, s in sorted(pair)[::-1]:
            # time: dist / speed
            t = float(target-p) / s
            if res and res[-1] >= t:
                continue
            res.append(t)
        return len(res)
        