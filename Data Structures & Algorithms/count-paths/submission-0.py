class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        optimal = {(m,n): 1}
        directions = [(1,0), (0,1)]

        def unique(x, y): 

            if (x,y) in optimal:
                return optimal[(x,y)]

            paths = 0

            for dx, dy in directions:
                nx, ny = (x + dx) ,(y + dy)

                if (nx, ny) in optimal:
                    paths += optimal[(nx, ny)]

                elif 1 <= nx <= m and 1 <= ny <= n:
                    path = unique(nx, ny)
                    optimal[(nx, ny)] = path
                    paths += path
            
            return paths
            
        return unique(1,1)
            
            

