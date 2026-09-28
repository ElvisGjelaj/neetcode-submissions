from collections import defaultdict
class Graph:
    
    def __init__(self):
        self.adj = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()

        def dfs(node):
            if node == dst:
                return True
            
            visited.add(node)

            if node in self.adj:
                for nxt_node in self.adj[node]:
                    if nxt_node not in visited and dfs(nxt_node):
                        return True
            
            return False

        return dfs(src)


