import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        t = 0

        while heap:
            e, r, c = heapq.heappop(heap)
            t = max(t, e)
            if r == ROWS - 1 and c == COLS - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
