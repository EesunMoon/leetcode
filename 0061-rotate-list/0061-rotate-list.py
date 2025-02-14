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

        # base case
        if not head:
            return head

        # 1) get total length O(n)
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        # 2) handle k
        k %= length
        if k == 0:
            return head

        # 3) split
        target = length - k
        curr = head
        for _ in range(target-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        
        # 4) connect new head and head
        curr= newHead
        while curr.next:
            curr = curr.next
        curr.next = head
        
        return newHead

