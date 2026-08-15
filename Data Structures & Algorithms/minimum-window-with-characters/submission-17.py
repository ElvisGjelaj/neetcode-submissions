class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_set = set(t)
        champ = s
        l = 0
        r = 1
        id = False
        while r < len(s) + 1:
            if id: print(s[l:r])
            if t_set.issubset(set(s[l:r])) and len(s[l:r]) < len(champ):
                champ = s[l:r]
                char = s[l]
                while char not in t_set:
                    l += 1
                    char = s[l]
                if len(s[l:r]) < len(champ):
                    champ = s[l:r]
                    print(champ)
                    id = True
                l += 1
            r += 1

        return champ
