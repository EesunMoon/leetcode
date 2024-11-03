class Solution(object):
    def reverseString(self, s):
        
        # print(s.reverse())
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                # print(s)
                helper(left+1, right-1)
        
        helper(0, len(s)-1)