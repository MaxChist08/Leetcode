# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        x = tmp
        new_elem = list1
        new_elem1 = list2
        while new_elem and new_elem1:
            if min(new_elem.val, new_elem1.val) == new_elem.val:
                x.next = new_elem
                new_elem = new_elem.next
            else:
                x.next = new_elem1
                new_elem1 = new_elem1.next
            x = x.next
        if new_elem:
            x.next = new_elem
        else:
            x.next = new_elem1
        return tmp.next