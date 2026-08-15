class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        for idx, char in enumerate(s):
            if idx == (length // 2):
                break
            if char != s[length -1 -  idx]:
                return False
        return True
