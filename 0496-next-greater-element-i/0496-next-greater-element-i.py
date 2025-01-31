class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using stack to determine how many
        count = {}
        stack = [] # save decreasing order

        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            count[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = count[nums1[i]]
        return nums1