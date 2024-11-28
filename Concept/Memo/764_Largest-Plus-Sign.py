class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        if len(mines) == n*n:
            return 0

        queue = deque()
        for r in range(1, n-1):
            for c in range(1, n-1):
                if [r, c] not in mines:
                    queue.append([r, c])
        
        largest = 1
        possible = (n-1)//2
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            r, c = deque.popleft(queue)
            for i in range(1, possible+1):
                for dirr, dirc in directions:
                    dirr *= r
                    dirc *= c
                    if dirr in (-1, n) or dirc in (-1, n):
                        break
                    else:
                        if [dirr, dirc] in mines:
                            break
            largest = max(largest, i)
        return largest
