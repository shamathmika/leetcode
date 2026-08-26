# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This is very easy. Two ways - copy the number to an array or string and reverse it to get
        the actual number, then add it really and create a new linked list with each of the digits.
        This adds O(N) space. So instead we can use two pointers and just create the new ll directly
        by just maintaining a sum and carry variables
        """
        ret = ListNode()
        cur = ret
        carry = 0
        while l1 != None or l2 != None or carry != 0: # This is same as while l1 and l2 or carry > 0
            s = 0
            s += l1.val if l1 else 0
            s += l2.val if l2 else 0
            s += carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ret.next
        # TC: O(N), SC: O(1)