# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        First we create a HEAD node and point it to the smaller number in the head of the two lists.
        Return HEAD.next. We need to have one pointer each for the two lists and one running pointer
        to make the actual final list. The pointers for both lists, lets call it p1 and p2. Compare
        the value of p1 and p2 and make running.next to point to the smaller one. Suppose p1 is smaller,
        move p1 to p1.next. Do these only until null. If either of the lists reaches null, then the other
        list has the remaining values
        """
        p1, p2 = list1, list2

        if not p1:
            return p2
        if not p2:
            return p1

        run = head = ListNode(-1, None)
        
        while p1 and p2:
            if p1.val <= p2.val:
                run.next = p1
                p1 = p1.next
            else:
                run.next = p2
                p2 = p2.next
            
            run = run.next

        run.next = p1 if p1 else p2

        return head.next
        # TC: O(N), SC:O(1)