class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        n = len(nums2), m = len(nums1)
        brute force: O(n*m) 
            for each nums1 iterate nums2 starting from last index to 0 by using nested loop
        
        storing next greater element using monotonic stack in hashmap
            hashmap- element: next greater element

            [1, 3, 4, 2]
                stack: if not stack, mapping -1 
                        before append stack, check stack[-1] > current num
                            if not: pop
                            if not stack -> mapping -1, otherwise -> mapping stack[-1]
                        append stack
        """
        # 1) fill hashmap using stack TC O(n), SC O(n)
        stack = []
        hashmap = {} # element: next greater element
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            hashmap[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        # 2) return result using hashmap TC O(n)
        for i, num in enumerate(nums1):
            nums1[i] = hashmap[num]
        return nums1