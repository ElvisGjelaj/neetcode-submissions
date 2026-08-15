# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def dfs(r, p, q):
            if p.val < r.val and q.val < r.val:
                return dfs(r.left, p, q)
            
            if p.val > r.val and q.val > r.val:
                return dfs(r.right, p, q)

            return r
        return dfs(root, p, q)


