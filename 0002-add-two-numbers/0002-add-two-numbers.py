# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        result = new_node = ListNode(0) # dummy node to start with

        while l1 or l2 or carry: # goes on until both of the numbers are over or there is a last carry
            if l1:
                carry += l1.val  # carry = 2 | 4 | 4
                l1 = l1.next
            if l2:
                carry += l2.val  # carry = 7 | 6 | 8
                l2 = l2.next
            
            carry, val = divmod(carry, 10) # carry = 7/10 = 0, val = 7%10 = 7 | carry = 10/10 = 1, val = 10%10 = 0 | carry = 0, val = 8

            new_node.next = ListNode(val) # creates a new node with the value and ensures the current one points to it
            new_node = new_node.next

        return result.next # ignore the dummy node with 0 created initially