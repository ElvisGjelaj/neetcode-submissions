from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights),len(heights[0])
        directions = [(0,-1), (0, 1), (-1, 0), (1, 0)]

        def bfs(starts):
            reachable = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()  
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                    (nr,nc) not in reachable and 
                    heights[nr][nc] >= heights[r][c] ):
                        queue.append((nr, nc))
                        reachable.add((nr,nc))

            return reachable

        pacific_starts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlantic_starts = [(ROWS - 1, c) for c in range(COLS)] + [(r, COLS - 1) for r in range(ROWS)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r,c] for r, c in pacific & atlantic]









