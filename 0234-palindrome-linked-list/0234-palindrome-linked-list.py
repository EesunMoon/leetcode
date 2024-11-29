# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        self.front = head

        def recursive(curr_node = head):
            if curr_node is not None:
                if not recursive(curr_node.next):
                    return False
                if self.front.val != curr_node.val:
                    return False
                self.front = self.front.next
            return True
        
        return recursive()