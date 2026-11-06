class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n + 1)}
        for u, v, t in times:
            graph[u].append((v, t))

        dist = {}
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if node  in dist:
                continue
            
            dist[node] = time
            
            for v, t in graph[node]:
                if v not in dist:
                    heapq.heappush(heap, (time + t, v))
            
        
        return max(dist.values()) if len(dist) == n else -1


            


        
        