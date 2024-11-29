# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length = 1
        tmp = head
        while tmp:
            length += 1
            tmp=tmp.next
        
        middle = (length+1)//2
        length = 1

        while head:
            if length == middle:
                return head
            length += 1
            head = head.next
