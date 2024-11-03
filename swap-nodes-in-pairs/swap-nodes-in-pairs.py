# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head or not head.next:
            return head
        
        first = head
        second = head.next

        # swap - pointer
        first.next = self.swapPairs(second.next)
        second.next = first

        # now the head is the second node
        return second
        
        
