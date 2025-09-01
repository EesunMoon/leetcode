class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort in position
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(key=lambda x:x[0], reverse=True)

        stack = []
        for p, s in pair:
            time = (target-p)/s
            if not stack:
                stack.append(time)
                continue
            
            top = stack[-1]
            if top < time:
                stack.append(time)
        return len(stack)

