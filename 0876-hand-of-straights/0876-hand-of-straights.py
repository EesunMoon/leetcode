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
        
        for card in hand:
            # find the valid start card
            start = card
            while count.get(start-1,0):
                start -= 1
            
            while start <= card:
                while count[start]:
                    for next_card in range(start, start+groupSize):
                        if not count.get(next_card, 0):
                            return False
                        count[next_card] -= 1
                start += 1
        return True