# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next
        while slow is not fast:
            if fast is None:
                return False
            slow = slow.next
            try: fast = fast.next.next
            except: fast = fast.next
        return True
        