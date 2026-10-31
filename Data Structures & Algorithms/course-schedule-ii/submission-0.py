class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        visited = set()
        done = set()
        res = []
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        

        def dfs(crs):
            if crs in visited:
                return False
            
            if crs in done:
                return True

            visited.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre) == False: return False
            visited.remove(crs)

            res.append(crs)
            done.add(crs)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs): return []
        return res

