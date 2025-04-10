# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        curr =head
        
        while curr:
            prev = result
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            
            # swap
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
        
        return result.next