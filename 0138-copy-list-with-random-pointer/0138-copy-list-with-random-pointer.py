"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # TC O(N) SC O(N)
        hashmap = {None:None} # oldNode: newNode
        curr = head
        while curr:
            newNode = Node(curr.val)
            hashmap[curr] = newNode # oldNode: newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = hashmap[curr]
            newNode.next = hashmap[curr.next]
            newNode.random = hashmap[curr.random]

            curr = curr.next

        return hashmap[head]