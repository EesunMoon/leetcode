# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # length - k
        # k > length => prevent k = k%length
        # 0, 1, 2, 3, 4
        # 3, 4, 1, 2, 3
        if not head:
            return head

        # total length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        k %= length
        if k == 0:
            return head
            
        target = length - k
        curr = head
        for _ in range(target-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        
        curr= newHead
        while curr.next:
            curr = curr.next
        curr.next = head
        return newHead

