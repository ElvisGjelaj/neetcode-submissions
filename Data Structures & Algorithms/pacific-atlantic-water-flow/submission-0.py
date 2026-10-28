class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS, = len(heights), len(heights[0])
        directions = [(0,-1), (0, 1), (-1, 0), (1, 0)]
        res = []
        visited = set()


        def bfs(r, c):
            nonlocal pacific, atlantic
            curr_height = heights[r][c]
            visited.add((r,c))

            if pacific and atlantic:
                return 

            if (r == 0 or c == 0):
                pacific = True

            if (r == ROWS - 1 or c == COLS - 1):
                atlantic = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS
                 and heights[nr][nc] <= curr_height and 
                 (nr, nc) not in visited):
                    bfs(nr, nc)             


        for r in range(ROWS):
            for c in range(COLS):
                atlantic = False
                pacific = False
                bfs(r,c)
                visited.clear()
                
                if atlantic and pacific:
                    res.append([r,c])

        
        return res