# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseSubGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr_node = head
        prev_node = None

        while k > 0:
            nxt_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt_node
            k -= 1
        return prev_node, head, curr_node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:

            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if kth.next is None:
                    return dummy.next
            
            group_head = prev_group.next

            new_head, new_tail, new_group = self.reverseSubGroup(group_head, k)

            prev_group.next = new_head
            new_tail.next = new_group
            prev_group = new_tail
        
        
        







