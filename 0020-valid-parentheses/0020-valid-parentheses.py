class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s)%2 !=0:
            return False

        # data structure - stack
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}
        for bracket in s:

            if bracket in mapping:
                # if bracket is closing bracket
                top_element = stack.pop() if stack else "#"
                
                if mapping[bracket] != top_element:
                    return False
            else:
                # if bracket is open bracket > add to stack
                stack.append(bracket)
        
        return not stack
        