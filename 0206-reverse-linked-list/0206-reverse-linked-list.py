# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        prev, nxt = None, curr.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next if curr else None
            
        return prev

