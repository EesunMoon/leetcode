# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reversek(nodeHead):
            previous_node = None
            current_node = nodeHead
            for _ in range(k):
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            return previous_node
                
        dummy = ListNode() # dummy
        previous = dummy
        curr = head

        while curr:
            nxt = curr
            cnt = k
            while nxt and cnt > 0:
                nxt = nxt.next
                cnt -= 1
            # enough to reverse
            if cnt == 0:
                previous.next = reversek(curr) # return the head of reverse node
                curr.next = nxt # connect the two set of nodes
                previous = curr
                curr = curr.next # move pointer
            else:
                break
        
        return dummy.next