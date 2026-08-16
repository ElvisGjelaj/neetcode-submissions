# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None

        def dfs(r):
            nonlocal ans, k

            if not r or ans is not None:
                return 

            dfs(r.left)
            if ans: return 

            k -= 1
            if k == 0:
                ans = r.val
                return
            
            dfs(r.right)
            return 
        
        dfs(root)
        return ans



