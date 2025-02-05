class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
            1 => [1, 0] or [0, 1]
            0 => [1, 1] or [0, 0]

            derived[0] = original[0] XOR original[1]
            derived[1] = original[1] XOR original[2]
            dervied[2] = original[2] XOR original[0]

            => all original elements use twice
        """
        # Each derived appered one more time
        XOR = 0
        for elem in derived:
            XOR ^= elem
        return XOR == 0
