class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1) freqmap
        freqmap = {}
        for task in tasks:
            freqmap[task] = 1 + freqmap.get(task, 0)
        
        # 2) maxHeap TC O(log26)
        maxHeap = [-cnt for cnt in freqmap.values()]
        heapq.heapify(maxHeap)

        t = 0
        q = deque() # [-cnt, idleTime]
        while maxHeap or q:
            t += 1
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t+n])
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0]) # we can use this

        return t