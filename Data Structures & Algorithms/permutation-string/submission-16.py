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
                for val in s2_set:
                    if val in occurs and occurs[val] > 0:
                        occurs[val] -= 1
                    else:
                        break
                for val in occurs:
                    print(occurs[val])
                    if occurs[val] != 0:
                        break
                print(occurs)
                return True
        return False