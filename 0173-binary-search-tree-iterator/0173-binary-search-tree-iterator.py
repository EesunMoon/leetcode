# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.sorted_node = []
        self.index = -1
        self._inorder(root)
    
    def _inorder(self, root):
        if not root:
            return
        
        self._inorder(root.left)
        self.sorted_node.append(root.val)
        self._inorder(root.right)
        

    def next(self):
        """
        :rtype: int
        """
        self.index +=1
        return self.sorted_node[self.index]
        


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index + 1 < len(self.sorted_node)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()