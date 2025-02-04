class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # - cost[i-1] + gas[i]
        # greedy: maximum gas vs minimum cost
        # ex) gas [6, 1, 2] cost [7, 1, 1] => 1: 1, 1-1+2=2, 2-1+6 = 7
        #    differ [-1, 0, 1]
        # ex) gas [1, 5, 7] cost[2, 3, 5]
        #    differ [ -1, 2, 2]
        # ex) gas [1, 2, 3, 4, 5], cost [3 ,4 ,5, 1, 2]
        # differ [ -2, -2, -2, 3, 3]

        # base
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (-cost[i]+gas[i])
            if total < 0:
                total = 0
                res = i + 1
        return res
