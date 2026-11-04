
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        graph = {i:[] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)
            
            return True
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res