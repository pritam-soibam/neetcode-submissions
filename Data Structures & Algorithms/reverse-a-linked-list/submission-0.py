# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next    # save next for iteration.

            # main
            curr.next = prev    # point backwards | 2>1 | 3>2>1 | ...
            prev = curr         # prev=1, 2, 3, ...

            curr = next
        return prev