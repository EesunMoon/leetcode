class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0 # 0000

        # 32 bits
        for i in range(32):
            # track digit for each time
            bit = (n >> i) & 1
            
            # apply bit to output reverse order
            res = (bit << (31-i)) | res

        return res