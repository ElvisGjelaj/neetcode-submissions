class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [char.lower() for char in s if char.isalnum()]
        palidrome = list(reversed(alphanum))
        if palidrome == alphanum:
            return True
        else: 
            return False
