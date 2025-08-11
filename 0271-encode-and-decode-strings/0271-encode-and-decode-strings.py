class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # seperator '#' + length 'l' + s
        encodedStr = ''
        for w in strs:
            encodedStr += str(len(w))
            encodedStr += '#'
            encodedStr += w

        return encodedStr

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        start = 0
        while start < len(s):
            # find length of words
            length = ""
            while s[start] != '#':
                length += s[start]
                start += 1
            
            # renew index
            start += 1
            length = int(length)
            decoded.append(s[start:start+length])
            start += length
        return decoded



        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))