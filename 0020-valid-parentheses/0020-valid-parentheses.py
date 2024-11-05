class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or (char == ")" and stack[-1] !="(") or (char == "}" and stack[-1]!="{") or (char == "]" and stack[-1]!="["):
                    return False
                stack.pop()
        
        return not stack





        """
        # Solution 2

        stack = []
        for c in s:

            if c in "({[": # open bracket
                stack.append(c)

            else: # close bracket
                if not stack or (c==')' and stack[-1]!='(') or (c==']' and stack[-1]!='[') or (c=='}' and stack[-1]!='{'):
                    return False
                stack.pop()
        
        return not stack
        """
        """
        # Solution 1

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
        """