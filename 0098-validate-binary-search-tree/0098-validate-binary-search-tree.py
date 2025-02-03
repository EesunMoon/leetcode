# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # calculate maximum of left subtree and minimum of right subtree
        # leftSubtree: root is the biggest
        # rightSubtree: root is the smallest
        """
        def valid(node, minimum, maximum):
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        return valid(root, float("-INF"), float("INF"))
        """

        if not root:
            return True

        # DFS - stack
        """
        stack = [[root, float("-INF"), float("INF")]]
        while stack:
            node, minimum, maximum = stack.pop()

            if not (minimum < node.val < maximum):
                return False
            if node.left:
                stack.append([node.left, minimum, node.val])
            if node.right:
                stack.append([node.right, node.val, maximum])
        return True
        """

        queue = deque()
        queue.append([root, float("-INF"), float("INF")])
        while queue:
            node, minimum, maximum = queue.popleft()
            if not (minimum < node.val < maximum):
                return False
            if node.left:
                queue.append([node.left, minimum, node.val])
            if node.right:
                queue.append([node.right, node.val, maximum])
        return True