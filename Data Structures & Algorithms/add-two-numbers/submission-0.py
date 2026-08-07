# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        num1, num2 = "", ""
        while n1 and n2:
            num1 += str(n1.val)
            n1 = n1.next

            num2 += str(n2.val)
            n2 = n2.next
        if n1:
            while n1:
                num1 += str(n1.val)
                n1 = n1.next
        else: 
            while n2:
                num2 += str(n2.val)
                n2 = n2.next
        
        total = str(int(num1[::-1]) + int(num2[::-1]))
        total = total[::-1]

        n = ListNode(total[0])
        root = n
        for i in range(1, len(total)):
            nxt_n = ListNode(total[i])
            n.next = nxt_n
            n = n.next

        return root

        
