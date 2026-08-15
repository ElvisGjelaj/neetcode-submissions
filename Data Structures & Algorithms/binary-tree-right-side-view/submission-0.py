from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_list = []
        queue = deque([root])
        
        if not root: return []

        while queue:
            level_sz = len(queue)
            right_list.append(queue[-1].val)
            
            for _ in range(level_sz):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right:queue.append(node.right)
            
        return right_list

        