# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_tree, right_tree = 0, 1

        # denote 0 as left subtree and 1 as right subtree
        def dfs(r, lower, upper):
            if not r:
                return True

            elif r.val > lower and r.val < upper:
                left = dfs(r.left, lower, r.val)
                right = dfs(r.right, r.val, upper)
                return left and right
            
            else: 
                return False

        return dfs(root, float("-inf"), float("inf"))
            