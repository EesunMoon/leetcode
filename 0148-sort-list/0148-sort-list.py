# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # find middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split into two partition
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeTwoLists(left, right)
        
        """
        # TC O(nlogn) SC O(n)
        # hashmap: (val: address)
        hashmap = {}
        curr = head
        while curr:
            hashmap[curr.val] = curr
            curr = curr.next

        # sorting
        hashmap = sorted(hashmap.items(), key=lambda x:x[0])
        
        dummy = ListNode()
        curr = dummy
        for v, node in hashmap:
            curr.next = node
            curr = curr.next

        return dummy.next
        """