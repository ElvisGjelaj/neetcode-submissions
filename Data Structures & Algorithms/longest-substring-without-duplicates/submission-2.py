class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLength = 0
        currLength = 0
        for char in s:
            if char not in substring:
                substring += char
                currLength += 1
            else:
                substring = char
                currLength = 1
            maxLength = max(maxLength, currLength)
                
        return maxLength
