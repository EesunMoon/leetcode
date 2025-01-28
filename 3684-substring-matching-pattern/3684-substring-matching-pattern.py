class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prior, after = p.split("*")

        if not prior:
            return after in s
        
        if not after:
            return prior in s
        
        if s.find(prior) != -1:
            if s.find(after, s.find(prior) + len(prior)) != -1:
                return True
        return False
        
        """
        # find prior string
        flag = False
        idx = 0
        for i in range(len(s)-len(prior)+1):
            if s[i:i+len(prior)] == prior:
                flag = True
                idx = i + len(prior)
                break
        
        # do not find prior string
        if not flag:
            return False
        
        # check after string
        if not after or after in s[idx:]:
            return True
        else:
            return False
        """