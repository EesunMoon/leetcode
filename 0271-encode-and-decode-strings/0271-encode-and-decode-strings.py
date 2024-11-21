class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        start = 0
        result = []
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            
            length = int(s[start:end])
            start = end + 1
            end = start + length
            result.append(s[start:end])
            start = end
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))