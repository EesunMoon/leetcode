class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        # using 2 hashmaps
        map_char = {}
        map_word = {}
        
        words = s.split()
        
        # base case
        if len(pattern) != len(words):
            return False
        
        for char, word in zip(pattern, words):
            if char not in map_char:
                if word in map_word:
                    return False
                else:
                    map_char[char] = word
                    map_word[word] = char
            else:
                if map_char[char] != word:
                    return False
        
        return True
        
