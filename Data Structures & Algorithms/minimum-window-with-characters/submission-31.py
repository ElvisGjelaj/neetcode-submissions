class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initialized HashMaps
        window = {}
        T = {}
        for char in t:
            window[char] = 0
            T[char] = T.get(char, 0) + 1
        l = 0
        need = len(t)
        have = 0
        res = None
        for r in range(0, len(s)):
            # moves r ptr
            char = s[r]
            char_num = T.get(char, 0)
            if char_num:
                window[char] = window.get(char, 0) + 1
                if window[char] == T[char]:
                    have += 1
            # moves l ptr and sets new res
            if have == need:
                champ = s[l:r+1]
                print(champ)
                if res is None: res = champ
                if len(res) > len(champ): res = champ
                while have == need:
                    char = s[l]
                    char_num = T.get(char, 0)
                    if char_num:
                        window[char] = window.get(char, 0) - 1
                        if window[char] < T[char]:
                            have -= 1
                    l -= 1
        if res is None: return ""
        else: return res
            
            


            
