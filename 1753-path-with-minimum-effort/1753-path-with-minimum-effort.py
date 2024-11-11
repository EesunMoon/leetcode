class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [[0,0,0]] # [weight, source, destination]
        n, m = len(heights), len(heights[0])
        visited = set()
        max_weight = 0

        while queue:
            weight, t_row, t_col = heapq.heappop(queue)
            if t_row == n-1 and t_col == m-1:
                return max(max_weight, weight)
            visited.add((t_row, t_col))
            max_weight = max(max_weight, weight)

            for row, col in direction:
                new_row = t_row + row
                new_col = t_col + col
                if (new_row in (-1, n) or new_col in (-1, m)) or (new_row, new_col) in visited:
                    continue
                new_weight = abs(heights[new_row][new_col]-heights[t_row][t_col])
                heapq.heappush(queue, [new_weight, new_row, new_col])

        return 0