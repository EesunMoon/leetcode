class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # base case
        if sum(gas) < sum(cost):
            return -1
        
        total, idx = 0, 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                idx = i + 1
                total = 0
        return idx