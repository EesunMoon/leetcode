class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = ""
        for num in digits:
            ans += str(num)
        ans = list(str(int(ans)+1))

        for i in range(len(ans)):
            ans[i] = int(ans[i])
        return ans