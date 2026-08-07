"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ptr_addrs = {}
        dc_n = Node(head.val)
        ptr_addrs[head] = dc_n
        nxt_n = head.next
        dc_head = dc_n
        while nxt_n:
            dc_nn = Node(nxt_n.val)
            dc_n.next = dc_nn
            ptr_addrs[nxt_n] = dc_nn
            dc_n = dc_n.next
            nxt_n = nxt_n.next
        dc_n.next = None

        # initializing random pts
        dc_node = dc_head
        og_node = head
        while dc_node:
            dc_node.random = ptr_addrs.get(og_node.random)
            dc_node = dc_node.next
            og_node = og_node.next
        
        return dc_head





            