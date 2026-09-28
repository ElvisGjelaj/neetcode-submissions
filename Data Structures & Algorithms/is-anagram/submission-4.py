class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for key in s:
            s_map[key] = s_map.get(key, 0) + 1

        for key in t:
            t_map[key] = t_map.get(key, 0) + 1
        
        return t_map == s_map
        