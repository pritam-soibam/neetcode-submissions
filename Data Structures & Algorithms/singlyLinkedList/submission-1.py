class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def getNode(self, index):
        if index > self.length - 1:
            return -1
        elif index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        else:
            i = 0
            node = self.head
            while i < index:
                node = node.next
                i += 1
            return node
    def get(self, index):
        result = self.getNode(index)
        return result.val if result != -1 else result

    def insertHead(self, val):
        if self.length == 0:
            new_node = ListNode(val)
            self.head = self.tail = new_node
            self.length = 1
        else:
            old_node = self.head
            new_node = ListNode(val, next=old_node)
            self.head = new_node
            self.length += 1

    def insertTail(self, val):
        if self.length == 0:
            new_node = ListNode(val)
            self.head = self.tail = new_node
            self.length = 1
        else:
            new_node = ListNode(val)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def remove(self, index):
        if index > self.length - 1:
            return False
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            prev = self.getNode(index - 1)
            prev.next = prev.next.next
            self.length -= 1
        return True

    def getValues(self):
        result = []

        node = self.head
        while node:
            result.append(node.val)
            node = node.next
        return result
