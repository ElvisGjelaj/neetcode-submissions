# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        champ = float("-inf")

        def dfs(r):
            nonlocal champ

            if not r:
                return 0
            
            left = dfs(r.left)
            right = dfs(r.right)
            champ = max(
                champ, r.val + max(left, 0) + max(right, 0)
            )
            return r.val + max(left, right, 0)
        
        dfs(root)
        return champ



