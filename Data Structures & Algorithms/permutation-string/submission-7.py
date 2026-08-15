class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        for i in range(len(s2) - length):
            s1_set = set(s1)
            s2_set = set(s2)
            if s1_set == s2_set:
                occurs = {}
                for num in s1:
                    if num in occurs: 
                        occurs[num] +=1
                    else:
                        occurs[num] = 1
                for num in s2:
                    if num in occurs:
                        occurs[num] -= 1
                    else:
                        break
                return True
