# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
            3
        1       4
              2
        inorder =  [1, 3, 2, 4] -> [1, 2, 3, 4]
                       f  s
            5
          3     7
        1   4  6  8
        inorder = [1,3,4,5,6,7,8]

            5
          3    4
        1   7  6  8
        inorder = [1, 3, 7, 5, 6, 4, 8] -> find last point that violate the constraints
                         f        s
        exactly two nodes of the tree were swapped => can be at most two points

        [high-level approach] inorder -> save the array, then find first and second condition
         => TC O(N) SC O(N)

        [optimization approach] using pointer first, second directly
        not using the sorted array that save the inorder result
        """
        self.first, self.second = None, None
        self.prev = None
        ## optimize in the space complexity
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node # previous ptr update
            
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val



        ## High level approach: TC O(N) SC O(N)
        """
        # 1) make sorted array using inorder traversal
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node)
            inorder(node.right)
        inorder(root)

        # 2) find the points that violate
        first, second = None, None
        for i in range(len(arr)-1):
            if arr[i].val > arr[i+1].val:
                if not first:
                    first = arr[i]
                second = arr[i+1]
        first.val, second.val = second.val, first.val
        """