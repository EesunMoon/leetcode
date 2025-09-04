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
        hashmap = {}
        dummy = Node(0)
        curr, point = head, dummy

        while curr:
            newNode = Node(curr.val)
            hashmap[curr] = newNode # oldNode: newNode
            point.next = newNode

            curr = curr.next
            point = point.next

        curr, point = head, dummy.next
        while curr:
            target = curr.random # random can point None or any nodes
            if target:
                point.random = hashmap[target]

            curr = curr.next
            point = point.next

        return dummy.next