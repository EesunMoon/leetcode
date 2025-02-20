class TreeNode:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None
    self.nextRight = None

"""
    [Constraint]
        1. tree can be empty
        2. tree can be unbalanced? O
        3. init: node.nextRight = None
    Question: return the tree that contain nextRight
        leftmost = root
            1    -> None || prev = None -> 2, curr = 1, leftmost = None -> 2
         2    3  -> None || curr = 2(leftmost)->3, prev = None->4->5->6, leftmost = none->4
       4  5     6 -> None || curr = leftmost(4->5), prev = None->7->9, leftmost = None->7
            7     9 -> || 

            1    -> None :: level 0
         2    3  -> None :: level 1
       4       6 -> None :: level 2
    
    [High level approach] BFS using Queue
    prev = None
    for _ in range(len(Q)):
        node = Q.popleft()
        if prev: prev.nextRight = node
        prev = node
    Analysis: TC O(N) SC O(W = n/2) = O(n)


    [Optimal solution] without using Queue DS
            1    -> None
         2    3  -> None
       4  5     6 -> None
                
                 curr           leftMost(next level)    prev        nextRight
    1 iteration:    1              2                    None       (2->3)
        connect 2->3 before going to the next level
        if root.right: root.left.nextRight = root.right                                    
    2 iteration:    2              4                    None         
                    3              4                     4          (4->5)
                                                         5          (5->6)
        curr = leftmost, prev = None. leftmost = None << for set next level
        
        
        for child in [curr.left, curr.right]:
            if child:
                if not prev: << the starting node in the next level
                    leftmost = child
                else:
                    prev.nextRight = child
                prev = child                             

"""
def optimal_solution(root):
    # base case
    if not root:
        return None

    leftmost = root # act as be setting at the previous level
    while leftmost:
        curr = leftmost
        prev, leftmost = None, None
        
        while curr:

            # track node
            for child in [curr.left, curr.right]:
                if child:
                    if not prev:
                        leftmost = child
                    else:
                        prev.nextRight = child
                    prev = child
            curr = curr.nextRight
    return root

def solution(root):
    # base case
    if not root:
        return None

    # BFS using Queue
    Q = deque([root])
    while Q:
        Q_len = len(Q)

        ## level search
        # search the node of next level using current level's nodes
        prev = None
        for _ in range(Q_len):
            node = Q.popleft()

            # connect previous node's nextRight pointer to current node
            if prev:
                prev.nextRight = node
            prev = node

            # append next node
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
    return root
