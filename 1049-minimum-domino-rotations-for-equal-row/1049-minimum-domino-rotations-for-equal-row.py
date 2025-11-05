class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        calculate the frequency both in tops and bottoms
        tops: 2:set(0,3,5,6), 1:1, 4:1
        bottoms: 5:1, 2:3, 6:1,3:1
        total Sum: 
        heap []
        1. maximum total freq of sum < 6 --> invalid
        2. 
        """
        topMap = defaultdict(set) # num: idx set O(N)
        bottomMap = defaultdict(set)
        totalFreq = {} # num: freq O(6)
        n = len(tops)
        for i in range(n):
            topMap[tops[i]].add(i)
            bottomMap[bottoms[i]].add(i)
            totalFreq[tops[i]] = 1 + totalFreq.get(tops[i], 0)
            totalFreq[bottoms[i]] = 1 + totalFreq.get(bottoms[i], 0)
        
        maxHeap = [] # O(6log6) maxHeap
        for num, freq in totalFreq.items():
            heapq.heappush(maxHeap, (-freq, num))
        
        if -maxHeap[0][0] < n:
            return -1

        while maxHeap:
            freq, num = heapq.heappop(maxHeap)
            if -freq < n:
                return -1
            topSet = topMap[num]
            bottomSet = bottomMap[num]
            common = topSet.intersection(bottomSet)
            if len(topSet) + len(bottomSet) - len(common) >= n:
                return min(len(bottomSet) - len(common), len(topSet)-len(common))
            
        return -1
