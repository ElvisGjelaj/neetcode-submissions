class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for char in s1:
            count[char] = 1 + count.get(char, 0)