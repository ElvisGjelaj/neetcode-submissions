class Node():
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.array = [-1] * 9901

    def put(self, key: int, value: int) -> None:
        bucket = key // 101 
        if self.array[bucket] == -1:
            self.array[bucket] = Node(key, value)
            return
        
        node = self.array[bucket]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        node = self.array[bucket]
        self.array[bucket] = Node(key, value, node)
        

    def get(self, key: int) -> int:
        bucket = key // 101
        node = self.array[bucket]
        if node == -1:
            return -1
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        bucket = key // 101
        node = self.array[bucket]
        if node == -1: 
            return 
        if node.key == key:
            if node.next == None:
                self.array[bucket] = -1
            else :
                self.array[bucket] = node.next
            return 
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
                

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)