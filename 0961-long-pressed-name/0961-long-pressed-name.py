class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        aaaalex, aaaaalleex
            l         lr
        aaaa, l, e, x
        aaaaa, ll, ee, x
        saeed, ssaaedd
        1. use the sliding window
        2. compare each sliding window
            - length: nameS <= typedS
            - char: same
        """
        if len(name) > len(typed):
            return False
        lName, rName = 0, 0
        lTyped, rTyped = 0, 0
        while rName < len(name) and rTyped < len(typed):
            if name[lName] != typed[lTyped]:
                return False

            while (rName+1) < len(name) and name[rName] == name[rName+1]:
                rName += 1

            while (rTyped+1) < len(typed) and typed[rTyped] == typed[rTyped+1]:
                rTyped += 1
            
            if (rName-lName+1) > (rTyped-lTyped+1):
                return False
            
            rName += 1
            rTyped += 1
            lName, lTyped = rName, rTyped
        
        if rTyped == len(typed) and rName == len(name):
            return True
        return False
