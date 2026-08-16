# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        kth_smallest = None
        def dfs(r):
            nonlocal stack

            if not r:
                return
            
            dfs(r.right)
            stack.append(r.val)
            dfs(r.left)

        dfs(root)
        
        for _ in range(k):
            kth_smallest = stack.pop()
        
        return kth_smallest


                
