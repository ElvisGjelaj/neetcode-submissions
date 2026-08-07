# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2, carry = l1, l2, 0
        root = ListNode()
        tail = root

        while n1 or n2 or carry:
            num1 = n1.val if n1 else 0
            num2 = n2.val if n2 else 0
            summ = num1 + num2 + carry

            carry = summ // 10
            digit = summ % 10

            tail.next = ListNode(digit)
            tail = tail.next
        
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        return root.next
        
