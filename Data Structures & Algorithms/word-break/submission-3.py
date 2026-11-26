class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [None] * (n)
        
        def solve(i):
            found = False
            if i >= n:
                return True
            
            if memo[i] is not None:
                return memo[i]
            
            for word in wordDict:
                m = len(word)
                if s[i:i + m] == word:
                    found = solve(i + m)
                    memo[i] = found
                    if found:
                        return found
            
            return found
        
        return solve(0)


