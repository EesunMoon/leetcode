class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use most frequently element first <- maxHeap (freq)
        # tracking the interval <- Queue ([freq, time])

        # define hashmap O(n)
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        # define max_heap, deque
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        Q = deque() # store [freq, time to be able to use]
        
        time = 0
        while max_heap or Q:
            time += 1
            if max_heap:
                freq = 1 + heapq.heappop(max_heap) # max heap
                if freq:
                    Q.append([freq, time+n]) 
            
            # use this task
            if Q and Q[0][1] == time:
                freq, t = Q.popleft()
                heapq.heappush(max_heap, freq)
        return time