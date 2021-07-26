class Node:
    def __init__(self):
        self.val = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        counter = 0
        start = self.head
        if index < len and index >= 0:
            while counter != index:
                start = start.next
                counter += 1
            return start.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        newHead = Node()
        newHead.val = val
        newHead.next = self.head
        self.head = newHead
        self.len += 1

    def addAtTail(self, val: int) -> None:
        newTail = Node()
        newHead.val = val
        end = self.head
        while end.next != None:
            end = end.next
        end.next = newTail
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        counter = 0
        newInd = Node()
        newInd.val = val
        start = self.head
        if index < len and index >= 0:
            while counter != index - 1:
                start = start.next
                counter += 1
            newInd.next = start.next
            start.next = newInd

        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        counter = 0
        start = self.head
        if index < self.len and index >= 0:
            while counter != index - 1:
                start = start.next
                counter += 1
            deleted = start.next
            start.next = deleted.next
        self.len -= 1

obj = MyLinkedList()
param_1 = obj.get(2)
obj.addAtHead(2)
obj.addAtTail(3)
obj.addAtIndex(1,4)
# obj.deleteAtIndex(index)



