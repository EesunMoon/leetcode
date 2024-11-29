class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashmap = collections.defaultdict(list)
        
        for string in strs:
            nums = [0] * 26
            for c in string:
                nums[ord(c)-ord('a')] += 1
            
            hashmap[tuple(nums)].append(string)
        
        return hashmap.values()

