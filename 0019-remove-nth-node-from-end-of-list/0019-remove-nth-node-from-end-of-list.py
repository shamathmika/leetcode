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
        # Two approaches with O(n) solution
        # 1. We find the length of the linked list and then delete the (len - n)th node
        # 2. Keep two pointers - one at the start and one n steps ahead. Then move them both to next node in each iteration
        # until the ahead one reaches null. Then delete the node right after the slower one
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy # We start this way for cases where there is only one node and we need to delete that
        for i in range(n): # This goes to 1st index if n=2. So head and head.next
            fast = fast.next
        
        while fast.next: # Keep it moving one by one once we have found out the nth node from the start until fast.next is not None. This is because, when fast.next = None, slow would be at the node just before the node that needs to be deleted
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next # Make the slow node skip the next node in the list

        return dummy.next

# TC: O(n)
# SC: O(1)