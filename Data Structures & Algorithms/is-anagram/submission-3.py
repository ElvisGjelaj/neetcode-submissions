class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for s_char in s:
            try:
                chars[s_char] += 1
            except KeyError:
                chars[s_char] = 1
        for t_char in t:
            try:
                chars[t_char] -= 1
            except KeyError:
                return False
        return all(value == 0 for value in chars.values())