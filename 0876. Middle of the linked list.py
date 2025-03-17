# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """x = head
        k = 1
        while (x.next):
            k += 1
            x = x.next
        for i in range(k // 2):
            head = head.next
        return head"""

        x = head
        x1 = head
        while x1.next and x1.next.next:
            x = x.next
            x1 = x1.next.next
        if x1.next:
            return x.next
        else:
            return x

