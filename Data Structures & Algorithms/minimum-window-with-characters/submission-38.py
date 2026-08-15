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
        res = ""
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
                while have == need:
                    char = s[l]
                    char_num = T.get(char, 0)
                    if char_num:
                        window[char] = window.get(char, 0) - 1
                        if window[char] < T[char]:
                            have -= 1
                    l -= 1

                champ = s[l:r+1]
                if len(res) == 0: res = champ
                elif len(res) > len(champ): res = champ
        if res is None: return ""
        else: return res
            
            


            
