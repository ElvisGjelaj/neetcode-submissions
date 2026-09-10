class Node:
    def __init__(self, key: int, value: int, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity


    def insert(self, key: int, value: int) -> None:
        idx = key % self.capacity
        curr = self.arr[idx]

        while curr:
            if curr.key == key:
                curr.value = value
                return

            curr = curr.next

        if (self.size + 1) / self.capacity >= 0.5:
            self.resize()
            idx = key % self.capacity

        new_node = Node(key, value, self.arr[idx])
        self.arr[idx] = new_node
        self.size += 1


    def get(self, key: int) -> int:
        idx = key % self.capacity
        curr = self.arr[idx]

        while curr:
            if curr.key == key:
                return curr.value

            curr = curr.next

        return -1


    def remove(self, key: int) -> bool:
        idx = key % self.capacity
        curr = self.arr[idx]
        prev = None

        while curr:
            if curr.key == key:
                if prev is None:
                    self.arr[idx] = curr.next

                else:
                    prev.next = curr.next

                self.size -= 1
                return True

            prev = curr
            curr = curr.next

        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        old_arr = self.arr
        self.capacity *= 2
        self.arr = [None] * self.capacity

        for head in old_arr:
            curr = head

            while curr:
                next_node = curr.next
                idx = curr.key % self.capacity

                curr.next = self.arr[idx]
                self.arr[idx] = curr
                curr = next_node


