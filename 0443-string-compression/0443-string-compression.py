class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        aabbcccaa
          l
          r
        a2b2c3a2 => 4
        """
        i = 0
        res = 0
        while i < len(chars):
            # find a character
            length = 1
            while (i+length < len(chars) and chars[i+length]==chars[i]):
                length += 1
            chars[res] = chars[i]
            res += 1
            
            if length > 1:
                str_length = str(length)
                chars[res:res+len(str_length)] = list(str_length)
                res += len(str_length)
            i += length
        return res
