"""
    Given a binary tree, 
    the task is to connect the nodes that are at the same level. 
    
    Given an addition nextRight pointer for the same.
    Initially, all the next right pointers point to garbage values, 
    set these pointers to the point next right for each node.

    https://www.geeksforgeeks.org/connect-nodes-at-same-level/
"""
import collections
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None ## implement this pointer

def optimal_solution(root):
    """
    use nextRight pointer
    TC O(n) SC O(1)

    [Move node at the same level] through nextRight pointer
    [Access to the node at the next level] current node's (children) left / right pointer
        [Connect the node at the same level] using 'prev' pointer
        [Stating from the first node at the next level] using 'leftmost' pointer

    1. For each level: set leftmost pointer and connect the node USING 'prev' pointer
            Since not using the queue that requires to move to the next node, USE 'nextRight' pointer
    2. For each node: set information related to next Level by tracking the childern of current node
            LeftMost value at the NEXT Level: if prev is EMPTY
    """

    # base case
    if not root:
        return None

    # Traversal without Queue
    # => set LeftMost, prev
    leftmost = root
    while leftmost:
        curr = leftmost # starting point
        prev = None
        leftmost = None # init for the next level
        
        # for each level
        while curr:

            # for each node:
            for child in [curr.left, curr.right]:
                if child:
                    if not prev:
                        leftmost = child
                    else:
                        prev.nextRight = child
                    prev = child # update
            
            # move to the next node at the same node
            curr = curr.nextRight
    return root

def solution(root):
    """
    # can be empty
        1 -> Null :: level 0
      2 -> 3 -> Null :: level 1
    4-> 5  ->  6 -> Null :: level 2

         1 -> Null
      2 -> Null
        5  ->  6 -> Null

        1 -> Null
      2 -> 3 -> Null
    4 -> Null

    # BFS TC O(n) SC O(n) n: #. of node in tree
    1. the node in the right side :: nextRight = Null
    2. level search using BFS
        level 0: 1
        level 1: 2, 3
        level 2: 4, 5, 6
    """
    # base case
    if not root:
        return []
    
    Q = collections.deque([root])
    while Q:
        size = len(Q)
        prev = None
        
        # level search
        for _ in range(size):
            node = Q.popleft()
            
            # connect current node to the prev node's nextRight pointer
            if prev:
                prev.nextRight = node
            prev = node

            # track next
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)

    return root
    


if __name__=="__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
