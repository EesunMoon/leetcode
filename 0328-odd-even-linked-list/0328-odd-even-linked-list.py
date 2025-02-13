# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        odd = head
        even = head.next
        dummy = even # even head

        while even and even.next:
            # linked odd
            odd.next = even.next

            # linked even
            odd = odd.next
            even.next = odd.next

            # move pointer
            even = even.next
            
        odd.next = dummy
    
        return head