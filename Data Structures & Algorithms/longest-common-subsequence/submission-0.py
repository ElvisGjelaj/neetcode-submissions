class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i, j = 0, 0
        n, m = len(text1), len(text2)
        memo = {}

        def rec(i, j):
            lcs = 0

            if i >= n or j >= m:
                return lcs
            
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                lcs += 1 + rec(i + 1, j + 1)
                memo[(i, j)] = lcs
            
            if text1[i] != text2[j]:
                lcs += max(rec(i + 1, j), rec(i, j + 1))
                memo[(i, j)] = lcs
            
            return lcs
        
        return rec(0, 0)
            

            
