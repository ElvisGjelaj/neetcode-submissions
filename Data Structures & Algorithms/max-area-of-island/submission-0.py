class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def bfs(r, c):
            nonlocal curr_area
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            curr_area += 1
            
            while q:
                r, c = q.popleft()
                directions = [[-1,0], [1, 0], [0, -1], [0,1]]

                for dr, dc in directions:
                    if ((r + dr) in range(ROWS) and (c + dc) in range(COLS) and 
                    (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == 1):

                        visited.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))
                        curr_area += 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = 0
                    bfs(r,c)
                    max_area = max(curr_area, max_area)

        return max_area

                    