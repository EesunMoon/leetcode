class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm = [[]]
        
        for n in nums:
            new_perm = []
            for p in perm:
                for i in range(len(p)+1):
                    p_copy = p[::]
                    p_copy.insert(i, n)
                    new_perm.append(p_copy)
            perm = new_perm
        
        return perm