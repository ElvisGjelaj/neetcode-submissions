import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Adjacency list
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([d, j])
                adj[j].append([d, i])

        # Prim's with min-heap
        res = 0
        visit = set()
        min_heap = [[0, 0]]  

        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue      
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(min_heap, [nei_cost, nei])

        return res