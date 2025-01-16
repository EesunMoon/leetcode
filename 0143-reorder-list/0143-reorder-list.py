# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # phase 1) split first, second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second, prev = slow.next, None # second half
        slow.next = None # first half

        # phase 2) reverse second portion
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # phase 3) merge first and second
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2