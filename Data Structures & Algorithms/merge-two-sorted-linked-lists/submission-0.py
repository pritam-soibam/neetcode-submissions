# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur = dummy_node
        while list1 or list2:
            if list1 and list2:
                n1 = list1.val
                n2 = list2.val
                if n1 < n2:
                    new_node = ListNode(n1)
                    list1 = list1.next
                else:
                    new_node = ListNode(n2)
                    list2 = list2.next

                cur.next = new_node
                cur = cur.next

            elif list1:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            elif list2:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
        return dummy_node.next