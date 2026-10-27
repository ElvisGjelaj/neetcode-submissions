class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        fresh = sum(row.count(FRESH) for row in grid)
        time = 0

        while fresh > 0:
            to_rot = []
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == ROTTEN:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == FRESH:
                                to_rot.append((nr, nc))

            if not to_rot:          # nothing changed this minute
                return -1

            for r, c in to_rot:
                if grid[r][c] == FRESH:   # an orange can be added twice
                    grid[r][c] = ROTTEN
                    fresh -= 1
            time += 1

        return time


