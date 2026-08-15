class Solution:
    def minWindow(self, s: str, t: str) -> str:
        champ = [0] * 1001
        l = 0
        r = 1
        while r < len(s) + 1:
            if t in s[l:r]:
                champ = s[l:r]
                char = s[l]
                while char not in t:
                    l += 1
                    char = s[l]
                if len(s[l:r]) < len(champ):
                    champ = s[l:r]
                    print(champ)
                l += 1
            r += 1
        if len(champ) > 1000: return ""
        else: return champ
