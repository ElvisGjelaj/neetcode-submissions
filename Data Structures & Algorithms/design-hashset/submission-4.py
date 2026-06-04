class MyHashSet:

    def __init__(self):
        self.array = [0] * 101

    # row is which 9901
    def add(self, key: int) -> None:
        row = key // 9901
        col = key % 9901
        self.array[row] |= (1 << col)

    def remove(self, key: int) -> None:
        row = key // 9901
        col = key % 9901
        self.array[row] &= ~(1<<col)

    def contains(self, key: int) -> bool:
        row = key // 9901
        col = key % 9901
        return (self.array[row] & (1 << col)) != 0



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)