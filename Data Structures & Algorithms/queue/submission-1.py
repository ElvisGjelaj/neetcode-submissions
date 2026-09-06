class ListNode:
    def __init__(self, value: int, prev: ListNode, nxt: ListNode):
        self.value = value
        self.prev = prev
        self.nxt = nxt


class Deque:
    
    def __init__(self):
        self.right = None
        self.left = None
        self.size = 0


    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else: 
            return False


    def append(self, value: int) -> None:
        # if first node added
        if self.size == 0:
            new_node = ListNode(value, None, None)
            self.right = new_node
            self.left = new_node
        else: 
            new_node = ListNode(value, self.right, None)
            self.right.nxt = new_node
            self.right = new_node
        
        self.size += 1

        
    def appendleft(self, value: int) -> None:
        # if first node added
        if self.size == 0:
            new_node = ListNode(value, None, None)
            self.left = new_node
            self.right = new_node
        else:
            new_node = ListNode(value, None, self.left)
            self.left.prev = new_node
            self.left = new_node
        
        self.size += 1


    def pop(self) -> int:
        
        if self.size == 0:
            return -1

        old_right = self.right
        new_right = self.right.prev
        self.right = new_right

        old_right.prev = None
        if new_right:
            new_right.nxt = None
        self.size -= 1
        return old_right.value


        
    def popleft(self) -> int:

        if self.size == 0:
            return -1

        old_left = self.left
        new_left = self.left.nxt
        self.left = new_left

        old_left.nxt = None
        if new_left:
            new_left.prev = None
        self.size -= 1
        return old_left.value



















        
