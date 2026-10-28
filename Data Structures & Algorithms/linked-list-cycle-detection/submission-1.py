# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def usingHash(self, head):
        seen = set()
        node = head
        while node:
            if node in seen:
                return True
            seen.add(node)
            node = node.next
        return False

    def usingTwoPointers(self, head):
        slow = fast = head
        # while fast is not None or fast.next is not None:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.usingTwoPointers(head)