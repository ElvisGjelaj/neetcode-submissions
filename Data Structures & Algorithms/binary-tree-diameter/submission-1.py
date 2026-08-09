# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return  1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        champ = 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        left_champ = self.diameterOfBinaryTree(root.left)
        right_champ = self.diameterOfBinaryTree(root.right)

        champ = max(leftDepth + rightDepth, max(left_champ, right_champ))
        return champ