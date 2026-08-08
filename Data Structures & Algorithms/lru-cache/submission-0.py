class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.sz = 0

        self.lru = Node()
        self.mru = Node()

        self.lru.next = self.mru
        self.mru.prev = self.lru


    def insert(self, node):
        # insert right before MRU dummy
        prev = self.mru.prev

        prev.next = node
        node.prev = prev

        node.next = self.mru
        self.mru.prev = node


    def remove(self, node):
        # remove this node from wherever it is
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # accessing it makes it most recently used
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # remove old node
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            # remove least recently used
            node = self.lru.next

            self.remove(node)
            del self.cache[node.key]

        
            

        
