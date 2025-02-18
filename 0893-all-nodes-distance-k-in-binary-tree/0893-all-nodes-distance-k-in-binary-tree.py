# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        without using adjacent graph
            -> should save the parent node information
        1. add parent information in each node: TC O(n)
        2. search based on parent pointer
        """
        # 1. add parent information in each node: TC O(n)
        def add_parent(curr, parent):
            if curr:
                curr.parent = parent
                add_parent(curr.left, curr)
                add_parent(curr.right, curr)
        add_parent(root, None)

        res = []
        seen = set()
        # 2. BFS
        Q = deque([(target, 0)])
        seen.add(target)
        while Q:
            if Q[0][1] == k:
                return [node.val for node, _ in Q]
            for _ in range(len(Q)):
                node, dist = Q.popleft()
                for next_node in [node.left, node.right, node.parent]:
                    if next_node and next_node not in seen:
                        Q.append([next_node, dist+1])
                        seen.add(next_node)
        return []

        # 2. DFS TC O(N) SC O(N)

        def dfs(curr, dist):
            # base case
            if not curr or curr in seen:
                return
            seen.add(curr)
            if dist == k:
                res.append(curr.val)
                return
            dfs(curr.parent, dist + 1)
            dfs(curr.left, dist + 1)
            dfs(curr.right, dist + 1)
        
        dfs(target, 0)
        return res
        
        """
        1. adjacent graph TC O(n) SC O(n)
        2. BFS TC O(n) SC O(n)
        """
        # 1. build adjacent graph
        adj = defaultdict(list)
        def makeGraph(node, parent):
            if parent:
                adj[node.val].append(parent.val)
            if node.left:
                adj[node.val].append(node.left.val)
                makeGraph(node.left, node)
            if node.right:
                adj[node.val].append(node.right.val)
                makeGraph(node.right, node)
        makeGraph(root, None)

        # 2. BFS- starting from target node
        Q = deque([target.val]) # append val
        seen = set()
        seen.add(target.val)
        while Q:
            if k == 0:
                return list(Q)
            for _ in range(len(Q)):
                node = Q.popleft()
                for nei in adj[node]:
                    if nei not in seen:
                        Q.append(nei)
                    seen.add(nei)
            k -= 1
        return []