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
        # can optimize using BSTIterator TC O(N) SC O(H)
        ## next function takes O(1) TC, O(H) SC
        ## hasNext function takes O(1) in both TC and SC
        # Recusion DFS TC O(N) SC O(N+H)
        seen = set()
        def dfs(node):
            if not node:
                return False
            if (k-node.val) in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

        
        # BFS TC O(N) SC O(N)
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
        

        # DFS - Stack TC O(N) SC O(N+H)
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