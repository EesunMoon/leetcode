class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        # count hashmap in s1 and s2
        hash1, hash2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            hash1[ord(s1[i])-ord("a")] += 1
            hash2[ord(s2[i])-ord("a")] += 1
        
        # matches or not?
        matches = 0
        for i in range(26):
            matches += (1 if hash1[i] == hash2[i] else 0)

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # increasing window (right)
            index = ord(s2[r]) - ord("a")
            hash2[index] += 1
            if hash1[index] == hash2[index]:
                matches += 1
            elif hash1[index]+1 == hash2[index]:
                matches -= 1
            
            # decreasing window (left)
            index = ord(s2[l]) - ord("a")
            hash2[index] -= 1
            if hash1[index] == hash2[index]:
                matches += 1
            elif hash1[index]-1 == hash2[index]:
                matches -= 1
            l += 1
        
        return matches == 26