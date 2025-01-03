class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        # base case
        if len(hand) % groupSize:
            return False
        
        # hashmap
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            # starting with the smallest value
            start = minH[0]

            for i in range(start, start+groupSize):
                # no exist consequence values
                if not count.get(i, 0):
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)
        return True