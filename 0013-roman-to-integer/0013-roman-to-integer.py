class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I >> V, X
        # X >> L, C
        # C >> D, M
        if not s:
            return 0

        symbol = list("IVXLCDM")
        value = [1, 5, 10, 50, 100, 500, 1000]
        s_dict = {k:v for k, v in zip(symbol, value)}
        print(s_dict)
        
        if len(s)==1:
            return s_dict[s]
        
        s_list = []
        # s_list = list(s)
        for idx in range(len(s)):
            if idx != len(s)-1:
                if s[idx] == "I" and (s[idx+1] == "V" or s[idx+1] == "X"):
                    s_list.append(-s_dict[s[idx]])
                elif s[idx] == "X" and (s[idx+1] == "L" or s[idx+1] == "C"):
                    s_list.append(-s_dict[s[idx]])
                elif s[idx] == "C" and (s[idx+1] == "D" or s[idx+1] == "M"):
                    s_list.append(-s_dict[s[idx]])
                else:
                    s_list.append(s_dict[s[idx]])
            else:
                s_list.append(s_dict[s[idx]])
        
        # print(s_list)
        # return sum(s_dict[k] for k in s_list)
        return sum(s_list)
        