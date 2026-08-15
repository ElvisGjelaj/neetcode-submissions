# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):
            if not subRoot and not root:
                return True

            if not subRoot or not root:
                return False
                
            if root.val == subRoot.val:
                left = dfs(root.left, subRoot.left)
                right = dfs(root.right, subRoot.right)
                return left and right
            
            else:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot)
