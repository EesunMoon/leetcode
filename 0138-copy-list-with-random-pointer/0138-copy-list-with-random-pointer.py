"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
            
        # phase 1) create copied list except for random pointer
        curr = head
        copy = Node(curr.val, None, None)
        dummy = Node(0, copy, None)
        address = {}

        address[curr] = copy
        curr = curr.next
        while curr:
            newNode = Node(curr.val, None, None)
            address[curr] = newNode
            copy.next = newNode
            copy = newNode
            curr = curr.next
        
        # phase 2) mapping random using hashmap
        newHead, curr = dummy.next, head
        while newHead:
            if curr.random:
                newHead.random = address[curr.random]
            newHead, curr = newHead.next, curr.next
        
        return dummy.next