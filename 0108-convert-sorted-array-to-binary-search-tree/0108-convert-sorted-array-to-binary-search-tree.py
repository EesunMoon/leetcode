# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # [-10, -3, 0, 5, 9]
        """
            preorder: parent -> left, right
            ** height-balanced
            [-10, -3, 0, 5, 9]
            l               r
                      m
            leftside (l ~ m-1)
            rightside (m+1 ~ r)

            base case) l > r => return
        """
        # TC O(N) SC O(H => logN)
        def makeGraph(l, r):
            # base case
            if l > r:
                return None
            
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = makeGraph(l, m-1)
            node.right = makeGraph(m+1, r)
            return node

        return makeGraph(0, len(nums)-1)
