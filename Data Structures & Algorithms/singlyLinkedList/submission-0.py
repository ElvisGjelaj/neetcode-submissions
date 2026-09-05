from typing import List


class ListNode:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt


class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.root

        for _ in range(index):
            curr = curr.nxt

        return curr.value

    def insertHead(self, val: int) -> None:
        self.root = ListNode(val, self.root)
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.root is None:
            self.root = new_node
            self.size += 1
            return

        curr = self.root

        while curr.nxt is not None:
            curr = curr.nxt

        curr.nxt = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        # if removing head
        if index == 0:
            self.root = self.root.nxt
            self.size -= 1
            return True

        prev = self.root
        curr = self.root.nxt

        for _ in range(1, index):
            prev = curr
            curr = curr.nxt

        prev.nxt = curr.nxt
        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.root

        while curr is not None:
            res.append(curr.value)
            curr = curr.nxt

        return res
