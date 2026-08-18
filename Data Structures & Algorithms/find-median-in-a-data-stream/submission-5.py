import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        if not self.max_heap:
             heapq.heappush_max(self.max_heap, num)
             return

        if num > self.max_heap[0]:
            heapq.heappush(self.min_heap, num)

        else: 
            heapq.heappush_max(self.max_heap, num)

        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            
            if len(self.max_heap) > len(self.min_heap):
                num = heapq.heappop_max(self.max_heap)
                heapq.heappush(self.min_heap, num)

            else:
                num = heapq.heappop(self.min_heap)
                heapq.heappush_max(self.max_heap, num)
        

    def findMedian(self) -> float:
        
        if abs(len(self.max_heap) - len(self.min_heap)) == 1:

            if len(self.max_heap) > len(self.min_heap):
                return float(self.max_heap[0])
            else:
                return float(self.min_heap[0])
        
        return (self.max_heap[0] + self.min_heap[0]) / 2
            