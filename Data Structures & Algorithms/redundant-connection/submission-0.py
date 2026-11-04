class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]   # path compression (halving)
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False    # already connected → this edge makes a cycle
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra     # attach smaller tree under larger
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
                    