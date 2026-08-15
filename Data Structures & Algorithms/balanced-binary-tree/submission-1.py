# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        return 1 + left + right
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)

        if left - right in [-1, 0, 1]:
            return True
        else:
            return False
        
        