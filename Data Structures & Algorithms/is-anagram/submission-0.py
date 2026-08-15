class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for s_char in s:
            chars[s_char] += 1
        
        for t_char in t:
            try:
                chars[t_char] -= 1
            except KeyError:
                return false
        return all(value == 0 for values in chars.values())