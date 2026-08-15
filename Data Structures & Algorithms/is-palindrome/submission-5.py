class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        for idx, char in enumerate(length// 2):
            if char != s[length -  idx]:
                return False
        return True
