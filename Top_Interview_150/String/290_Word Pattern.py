class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        
        s, pattern = s.split(), list(pattern)

        '''
            map(function, iterable1, iterable2, ...)
                function
                iterable: data
        '''
        
        print(map(s.index, s))
        print(map(pattern.index, pattern))
        
        return map(s.index, s) == map(pattern.index, pattern)
    
    
    
    '''
    # Using Hash Map
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
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
    '''
        
