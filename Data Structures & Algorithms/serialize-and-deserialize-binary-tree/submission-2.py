# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def dfs(r):
            nonlocal values

            if not r:
                values.append("#")
                return
            
            values.append(str(r.val))
            dfs(r.left)
            dfs(r.right)

        dfs(root)
        return ",".join(values)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        pre_idx = 0

        def dfs():
            nonlocal pre_idx

            if nodes[pre_idx] == "#":
                pre_idx += 1
                return None
            
            node = TreeNode(int(nodes[pre_idx]))
            pre_idx += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

            



