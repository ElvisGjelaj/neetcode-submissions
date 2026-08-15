class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [char for char in s if char.isalnum()]
        palidrome = "".join(reversed(alphanum))
        if palidrome == s:
            return True
        else: 
            return False
