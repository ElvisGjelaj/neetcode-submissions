# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        n1, n2 = list1, list2
        while n1 and n2:
            if n1.val < n2.val:
                tail.next = n1
                n1 = n1.next
            else: 
                tail.next = n2
                n2 = n2.next
            tail = tail.next
        if n1:
            tail.next = n1
        else:
            tail.next = n2
        return dummy.next
        
        
