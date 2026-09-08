from typing import List


class TreeNode:
    def __init__(self, key: int, value: int, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        curr = self.root

        if not curr:
            self.root = TreeNode(key, val)
            return

        while True:
            if key > curr.key and curr.right:
                curr = curr.right

            elif key < curr.key and curr.left:
                curr = curr.left

            elif key == curr.key:
                curr.value = val
                return

            else:
                break
        
        new_node = TreeNode(key, val)

        if key > curr.key:
            curr.right = new_node
        else: 
            curr.left = new_node


    def get(self, key: int) -> int:
        curr = self.root

        while curr is not None:
            if key == curr.key:
                return curr.value

            if key > curr.key:
                curr = curr.right
            else:
                curr = curr.left
        
        return -1


    def getMin(self) -> int:
        curr = self.root

        if curr is None:
            return -1

        while curr.left is not None:
            curr = curr.left
        
        return curr.value


    def getMax(self) -> int:
        curr = self.root

        if curr is None:
            return -1

        while curr.right is not None:
            curr = curr.right
        
        return curr.value


    def remove(self, key: int) -> None:
        """
        case 1: no children: set parent ptr to None
        case 2: 1 child: set parent ptr to child
        case 3: 2 children: replace node with lowest on right
        """

        # Find the node and its parent
        curr = self.root
        parent = None

        while curr is not None and curr.key != key:
            parent = curr

            if key > curr.key:
                curr = curr.right
            else:
                curr = curr.left

        # Key doesn't exist
        if curr is None:
            return

        # Case 3: two children
        if curr.left is not None and curr.right is not None:
            
            # Find smallest node in right subtree
            successor_parent = curr
            successor = curr.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # Copy successor into node we're "deleting"
            curr.key = successor.key
            curr.value = successor.value

            # Now delete the successor instead
            parent = successor_parent
            curr = successor

        # At this point curr has 0 or 1 child
        if curr.left is not None:
            child = curr.left
        else:
            child = curr.right

        # Removing root
        if parent is None:
            self.root = child

        # curr is parent's left child
        elif parent.left == curr:
            parent.left = child

        # curr is parent's right child
        else:
            parent.right = child


    def getInorderKeys(self) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.key)
            inorder(node.right)

        inorder(self.root)

        return result

