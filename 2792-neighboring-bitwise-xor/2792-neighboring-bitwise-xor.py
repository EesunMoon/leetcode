class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
            1 => [1, 0] or [0, 1]
            0 => [1, 1] or [0, 0]
        """
        # Each derived appered one more time
        XOR = 0
        for elem in derived:
            XOR ^= elem
        return XOR == 0
