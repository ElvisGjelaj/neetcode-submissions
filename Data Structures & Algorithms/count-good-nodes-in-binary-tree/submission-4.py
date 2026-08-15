from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(r, max_so_far):
            nonlocal good_nodes

            if not r:
                return
            
            if r.val >= max_so_far:
                good_nodes += 1
            
            max_so_far = max(max_so_far, r.val)

            dfs(r.left, max_so_far)
            dfs(r.right, max_so_far)

        dfs(root, float("-inf"))
        return good_nodes


