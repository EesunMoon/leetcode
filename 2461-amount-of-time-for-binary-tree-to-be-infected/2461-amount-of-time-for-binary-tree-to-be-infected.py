# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
            Not using adjacent list
            - save parent node information
            - infection is root: max(leftDepth, rightDepth)

            - infection is not root: 
                leaf: leftDepth + rightDepth + 1 (root)
                not leaf:
                    if in leftSubTree
                        max(leftDepth - depth(start~leaf)+rightDepth, depth(start~leaf))
                            leaf node:: depth(start~leaf)
                                        max(leftDepth+rightDepth)
        """
        if not root:
            return 0
        # 1. add parent
        self.starting = None
        def add_parent(curr, parent):
            if curr:
                curr.parent = parent
                if curr.val == start:
                    self.starting = curr
                add_parent(curr.left, curr)
                add_parent(curr.right, curr)
        add_parent(root, None)
        
        # 2. BFS
        res = -1
        seen = set([self.starting])
        Q = deque([self.starting])
        while Q:
            for _ in range(len(Q)):
                node = Q.popleft()
                for next_node in [node.left, node.right, node.parent]:
                    if next_node and next_node not in seen:
                        Q.append(next_node)
                        seen.add(next_node)
            res += 1
        return res
            
        

        """
            root = [1,5,3,null,4,10,6,9,2], start = 3
                    infected
            0 min: 3
            1 min: 3, 1, 6, 10
            2 min: 3, 1, 6, 10, 5
            3 min: 3, 1, 6, 10, 5, 4
            4 min: 3, 1, 6, 10, 5, 4, 9, 2 << finished

            Output: #.minute needed for the entir tree to be infected

            Constraint: start not in binary tree - gaurantee
                        input Unique? - gaurantee

            1. make adjacent graph: TC O(n), SC O(2n) -> O(n)
            2. using BFS (since the node affect other node as widely as possible)
                terminate condition) len(visited) == len(Node) or Q << O(n)
            total TC O(n) SC O(n)
        """

        # DFS not using Adjacent Node
        self.res = 0
        def dfs(node):
            if not node:
                return -1

            #search left and right subtree
            left = dfs(node.left)
            right = dfs(node.right)

            # find the starting point
            if node.val == start:
                self.res = max(left, right) + 1
                return 0
                
            if left >= 0:
                self.res = max(self.res, left+right)

        
        # Using BFS and Adjacent Node TC O(n) SC O(n)
        
        # 1) make adjacent graph: TC O(n) SC O(n)
        adj = defaultdict(list)
        def makeGraph(node, prev):
            if not node:
                return
            
            if prev:
                adj[node.val].append(prev.val)
            if node.left:
                adj[node.val].append(node.left.val)
            if node.right:
                adj[node.val].append(node.right.val)
                
            makeGraph(node.left, node)
            makeGraph(node.right, node)

        makeGraph(root, None)
        
        # 2) BFS
        res = 0
        visited = set([start])
        Q = deque([start])

        while Q and len(visited) < len(adj):
            for _ in range(len(Q)):
                node = Q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        Q.append(nei)
                        visited.add(nei)
            res += 1

        return res