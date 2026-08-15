class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_set = set(t)
        champ = s
        l = 0
        r = 1
        while r < len(s) + 1:
            if t_set.issubset(set(s[l:r])) and len(s[l:r]) < len(champ):
                champ = s[l:r]
                char = s[l]
                print(champ)
                while char not in t_set:
                    l += 1
                if len(s[l:r]) < len(champ):
                    champ = s[l:r]
                l += 1
            r += 1
        return champ
