class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # guaranteed to be unique
        # subSum > 0 :: start
        # total gas < total cost :: impossible

        # base case
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                res = i+1 # starting from next index
                total = 0
        return res