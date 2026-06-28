class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        for i in range(len(s2) - length + 1):
            s1_set = set(s1)
            s2_set = set(s2[i:i+length])
            if s1_set == s2_set:
                occurs = {}
                for val in s1:
                    if val in occurs: 
                        occurs[val] +=1
                    else:
                        occurs[val] = 1
                # check 1
                print(s1)
                for val in s2[i:i + length]:
                    if val in occurs:
                        occurs[val] -= 1
                    else:
                        break
                # check 2
                print(s2[i:i + length])
                good = True
                for val in occurs:
                    if occurs[val] != 0:
                        good = False
                if good: return True
        return False