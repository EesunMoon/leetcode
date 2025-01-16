# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # phase 1) reverse
        prev, tail = None, head
        while tail:
            tmp = tail.next
            tail.next = prev
            prev, tail = tail, tmp

        # phase 2) delete
        if n == 1:
            first = prev.next
        else:
            first = curr = prev # save first position
            prev, tmp = None, curr.next
            for i in range(1, n):
                prev = curr
                curr, tmp = curr.next, tmp.next
            prev.next = tmp

        # phase 3) reverse again - to return original head
        prev = None
        while first:
            tmp = first.next
            first.next = prev
            prev, first = first, tmp
        
        return prev
        