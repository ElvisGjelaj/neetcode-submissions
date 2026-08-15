class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rep = k
        idx = 1
        cmp_idx = 0
        maxLength = 0
        currLength = 1 
        currChar = s[0]
        while idx < len(s):
            if s[idx] == currChar:
                currLength += 1
            elif rep > 0:
                cmp_idx = idx if rep == k else cmp_idx
                rep -=1
                currLength += 1
            else: 
                currChar = s[cmp_idx]
                idx = cmp_idx + 1
                rep = k
                currLength = 1
            maxLength = max(currLength, maxLength)
            idx += 1
        return maxLength
        
