class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        used = [False] * len(s1)
        l = 0
        while l < len(s2):
            if s2[l] in s1 and used[list(s1).getindex(s1[l])] == False:
                used[s1.getinde(s1[l])] = True
                r = 0
                while r < len(s2):
                    if s2[r] in s1 and used[list(s1).getindex(s1[r])] == False:
                        used[s1.getinde(s1[r])] = True
                    elif not any(used):
                        return true
                    else: 
                        used = [False] * len(s1)
                        break
                    r += 1
            l += 1
        return false


