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
        hashmap = {} # existed: address
        dummy = Node(0)
        
        # copy key and next pointer
        prt = dummy
        curr = head
        while curr:
            NewNode = Node(curr.val) # make new node
            prt.next = NewNode # connect new node
            hashmap[curr] = NewNode # save in hashmap

            # move pointer both new pointer and existed pointer
            prt = prt.next
            curr = curr.next

        # copy random pointer
        prt = dummy.next
        curr = head
        while curr:
            rand = curr.random
            if rand:
                prt.random = hashmap[rand]

            prt = prt.next
            curr = curr.next
        
        return dummy.next