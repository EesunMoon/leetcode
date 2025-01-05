class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            start = minH[0]
            for num in range(start, start+groupSize):
                if num not in count:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    if num != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True