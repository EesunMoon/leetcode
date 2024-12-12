class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        flag = 1 # 1: increment, -1: decrement
        res = [[]*numRows for _ in range(numRows)]
        # print(res)
        p = 0

        for c in s:
            if p == 0:
                flag = 1
            
            res[p].append(c)
            if p == numRows-1:
                flag = -1
            
            p = p + 1*flag
        print(res)
        answer = ""
        for row in res:
            answer += "".join(row)

        return answer
        