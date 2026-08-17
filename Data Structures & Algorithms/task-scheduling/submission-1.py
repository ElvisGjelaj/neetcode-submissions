from collections import Counter
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = list(counts.values())
        heapq.heapify_max(max_heap)

        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                freq = heapq.heappop_max(max_heap)
                freq -= 1
                if freq > 0:
                    queue.append((freq, time + n))

            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush_max(max_heap, freq)

        return time

