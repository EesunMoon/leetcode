class Solution:
    def decodeString(self, s: str) -> str:
        # k[char]
        # k[char]k[char]
        # k[chark[char2]]
        """
        ex) 3[a2[c]]3[ab]
        3,[,a,2,[,c,
        3,[,a,cc
        accaccacc, ababab
            if meeting closing bracket::
                currChar --> pop elements from stack until appearing [ --> acc
                then, currK --> pop element stack is not none and not alpha --> 3
                currDecodedStr = currChar * currK
                    then, store currDecodedStr
        --
        if digit: calculate digit
        elif [: store k then init, store currStr then init
        elif ]: pop k then decoded with curr, then pop previous Curr concate
        else: concate curr digit
        """
        numStack = []
        charStack = []
        currK = 0
        currStr = ""

        for c in s: # 30[a2[b]]ab
            if c.isdigit(): 
                currK = currK*10 + int(c)
            elif c == "[": # numStack = [30], charStack = [""]ab
                numStack.append(currK)
                currK = 0
                charStack.append(currStr)
                currStr = ""
            elif c == "]": # decoded
                k = numStack.pop() # 30
                currDecoded = k*currStr # 
                currStr = charStack.pop()
                currStr += currDecoded 
            else:
                currStr += c # currStr = abb

        return currStr
        

