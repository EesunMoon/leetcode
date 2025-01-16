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

        # phase 1) create copied list except for pointer
        hashmap = {None:None} # base case
        curr = head
        while curr:
            newNode = Node(curr.val)
            hashmap[curr] = newNode
            curr = curr.next
        
        # phase 2) mapping random using hashmap
        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next
            
        return hashmap[head]