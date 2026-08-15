from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lot = []
        queue = deque([root])

        if not root:
            return []

        while queue:
            level = []
            level_sz = len(queue)

            for _ in range(level_sz):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            lot.append(level)
        
        return lot



