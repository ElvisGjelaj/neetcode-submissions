import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heap = [(math.sqrt((x)**2 + (y)**2), [x,y]) for [x,y] in points]

        heapq.heapify(heap)

        print(heap)
        for _ in range(k):
            closest.append(heapq.heappop(heap))

        
        return [close[1] for close in closest] 