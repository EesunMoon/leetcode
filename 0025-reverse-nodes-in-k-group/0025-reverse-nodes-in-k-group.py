# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head
        newHead, tail, nextNode = self.reverseList(curr, k)
        curr = nextNode
        while curr:
            newPrev, newTail, nextNode = self.reverseList(curr, k)
            tail.next = newPrev
            tail = newTail
            curr = nextNode

        return newHead
    
    def reverseList(self, node, k):
        prev = None
        tail = curr = node
        for i in range(k):
            if i< k-1 and not curr.next:
                return tail, None, None
            curr = curr.next

        curr = node
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev, tail, tmp # newHead, newTail, nextNode