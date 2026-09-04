class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        elem = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return elem

    def resize(self) -> None:
        new_arr = [None] * 2 * len(self.arr)
        self.capacity = 2 * self.capacity
        for idx, elem in enumerate(self.arr):
            new_arr[idx] = elem
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
