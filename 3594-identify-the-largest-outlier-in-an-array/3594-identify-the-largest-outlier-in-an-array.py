class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
            special number: n - 2 elements
            typical number: sum(n-2)
            outlier: other => sum(nums) - typical number * 2

            to find the typical number by using 'sum(nums) - typical number * 2'

            ex) 2, 3, 5, 10:: total = 20
            2: outlier = 16
            3: outlier = 11
            5: outlier = 10
        """

        total = sum(nums) # O(n)
        
        hashmap = {}
        # hashmap => O(n)
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        outlier = float("-INF")
        for num in hashmap.keys(): # consider as sum of special num
            cand_outlier = total - 2 * num # (sum of special num)
            if cand_outlier in hashmap:
                if cand_outlier != num or hashmap[cand_outlier] > 1:
                    outlier = max(outlier, cand_outlier)
        return outlier
        
        """
        # sorting + 
        nums.sort() # O(nlogn)

        # Brute force O(n^2)
        for i in range(len(nums)-1, -1, -1):
            outlier = nums[i]
            
            for j in range(len(nums)-1, -1, -1):
                if i == j:
                    continue
                special = total - outlier - nums[j]
                if special == nums[j]:
                    return outlier    
        """        