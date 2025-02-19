# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMin(self, node):
            leftmost = node
            while leftmost.left:
                leftmost = leftmost.left
            return leftmost

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return root
        
        # optimization TC O(N) SC O(1)
        # 1. find the node to delete
        parent, curr = None, root
        while curr:
            if curr.val > key:
                parent = curr
                curr = curr.left
            elif curr.val < key:
                parent = curr
                curr = curr.right
            else:
                # 2. delete node
                # case1) leaf
                if not curr.left and not curr.right:
                    if not parent: # root
                       return None
                    else: # not root
                        if parent.left == curr:
                            parent.left = None
                        else:
                            parent.right = None
                # case2) only one child
                elif not curr.left or not curr.right:      
                    child = curr.left if curr.left else curr.right
                    if not parent: # root
                        return child
                    else: # not root
                        if parent.left == curr:
                            parent.left = child
                        else:
                            parent.right = child
                # case3) have two children
                else:
                    leftmost = self.getMin(curr.right)
                    curr.val = leftmost.val
                    
                    # delete leftmost value in rightsubtree
                    parent = curr
                    curr = curr.right
                    key = leftmost.val
                    continue
                break
        return root
    
        """
        base case)
            1. not root
            2. not key in the tree
        
        [high level] TC O(N) SC O(H)
            1. find the node to delete: if not exist - return root O(N), O(1)
            2. delete node O(H), O(1)
                case 1) if leaf (no children): just delete O(1)
                case 2) if only one child: swap node to the child, delete child O(1)
                case 3) if two children: find minimum value(leftmost node) in the rightSubTree
        """


        # 1) find the node to delete
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2) delete node
            # case1) leaf node
            if not root.left and not root.right:
                return None
            # case2) only one child
            if not root.left or not root.right:
                return root.left if root.left else root.right
            # case3) all children exist
            else:
                # change with leftmost value in the rightSub
                leftmost = self.getMin(root.right)
                root.val = leftmost.val # update root to leftmost
                root.right = self.deleteNode(root.right, leftmost.val)
        return root