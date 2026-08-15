# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # count number of nodes
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        
        # removing the nth node from end
        count -= n
        if count == 0:
            return None
        prev, curr, nxt = None, head, head.next

        while count:
            prev = curr
            curr = nxt
            nxt = nxt.next
            count -= 1
        
        prev.next = nxt
        curr.nxt = None

        return head
        
        