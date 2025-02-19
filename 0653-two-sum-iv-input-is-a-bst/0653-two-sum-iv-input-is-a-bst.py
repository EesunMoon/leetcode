# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        seen = set()
        def dfs(node):
            if not node:
                return False
            if (k-node.val) in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

        
        # BFS O(n)
        """
        
        seen = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if (k - node.val) in seen:
                return True
            
            seen.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
        

        # DFS - Stack
        seen = set()
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            if (k - curr.val) in seen:
                return True
            seen.add(curr.val)

            curr = curr.right
        return False
        """