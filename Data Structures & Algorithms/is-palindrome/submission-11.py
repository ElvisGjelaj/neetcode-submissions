class Solution:
    def isPalindrome(self, s: str) -> bool:
        palidrome = "".join(reversed(s))
        if palidrome == s:
            return True
        else: return False
