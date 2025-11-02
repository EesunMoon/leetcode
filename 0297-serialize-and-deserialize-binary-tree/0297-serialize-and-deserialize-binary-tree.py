# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = ""
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res += (str(node.val)+"#")
                q.append(node.left)
                q.append(node.right)
            else:
                res += "N#"
        return res
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nums = data.split("#")
        root = TreeNode(int(nums[0]))
        q = deque([root])
        i = 1
        while q and i < len(nums):
            currNode = q.popleft()
            # left
            if nums[i] != "N":
                leftNode = TreeNode(int(nums[i]))
                currNode.left = leftNode
                q.append(leftNode)
            # right
            if nums[i+1] != "N":
                rightNode = TreeNode(int(nums[i+1]))
                currNode.right = rightNode
                q.append(rightNode)
            i += 2
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))