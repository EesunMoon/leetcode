class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        def findNeighbors(code):
            res = []
            for i in range(4):
                digit = str((int(code[i])+1)%10)
                res.append(code[:i]+digit+code[i+1:])
                digit = str((int(code[i])-1)%10)
                res.append(code[:i]+digit+code[i+1:])
            return res

        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        queue = deque([("0000", 0)])

        while queue:
            cand, steps = queue.popleft()
            if cand == target:
                return steps
            
            for neigh in findNeighbors(cand):
                if neigh not in visited:
                    queue.append((neigh, steps+1))
                    visited.add(neigh)

        return -1
        