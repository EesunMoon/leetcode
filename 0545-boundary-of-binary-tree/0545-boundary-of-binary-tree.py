# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
            root -> left boundary -> leaf -> right boundary (reversed)
                1. left boundary
                    - leftSubtree is None -> []
                        else -> left child
                    - left.right (o) -> right
                    - leftmost leaf -> left boundary(x), leaf(o)
                2. right boundary: reverse order of the right boundary
                    - rightSubtree is None -> []
                        else -> right child
                3. leaves 
                    - no child
                    - root is not leaf
            
            [output] the values of boundary of Binary tree
            
            [contraint]
            base case) tree can be empty
            
            [high-level] 
            - function
                1. isleaf: define whether the node is leaf or not (not root)
                    TC O(1) SC O(1)
                2. addLeftBoundary: starting from root.left, 
                                    iterate until left is empty or node is leaf
                                    by moving pointer to the left
                                        if not left -> right
                    TC O(H = N, logN, 0) SC O(1)
                3. addRightBoundary: starting from root.right
                                    iterate until right is empty or node is leaf
                                    and store the value using stack
                                    by moving pointer to the right.
                                    add the element(in right boundary) in reverse order
                                    by popping the stack
                    TC O(H) SC O(H)
                4. addLeaf: recursive dfs - inorder search
                            by iterating left, root, right
                            if the node isleaf -> add the value
                    TC O(N) SC O(H)
                => TOTAL: TC O(N) SC O(H)
            - algorithm
                1. track root - isleaf(root):: False
                2. track left boundary - call the addLeftBoundary(root.left)
                3. track leaf - call addLeaf(root)
                4. track right boundary - call the addRightBoundary(root.right)
        """
        res = [] # boundary of binary tree
        
        def isLeaf(node):
            return not node.left and not node.right
        
        def addLeftBoundary(node):
            curr = node
            while curr and not isLeaf(curr):
                res.append(curr.val)
                curr = curr.left if curr.left else curr.right
        
        def addRightBoundary(node):
            stack = []
            curr = node
            while curr and not isLeaf(curr):
                stack.append(curr.val)
                curr = curr.right if curr.right else curr.left
            while stack:
                res.append(stack.pop())
        
        def addLeaf(node):
            # base case
            if not node:
                return
            
            # add condition
            if isLeaf(node):
                res.append(node.val)
                return
            
            addLeaf(node.left)
            addLeaf(node.right)
        
        # base case
        if not root:
            return res
        
        # root
        if not isLeaf(root):
            res.append(root.val)
        
        # left boundary
        addLeftBoundary(root.left)
        
        # leaf
        addLeaf(root)
        
        # right boundary
        addRightBoundary(root.right)
        
        return res