class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLength = 0
        currLength = 0
        for char in s:
            if char not in substring:
                substring += char
                length += 1
            else:
                substring = char
                maxLength = max(maxLength, currLength)
                currLength = 1
