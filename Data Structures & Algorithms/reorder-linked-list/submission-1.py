# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding the middle pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # reversing 2nd list
        curr, prev = slow.next, None
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #merging two lists
        l1, l2 = head, prev
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        else: tail.next = l2


        




        