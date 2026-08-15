class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [char for char in s if char.isalnum()]
        palidrome = list(reversed(alphanum))
        if palidrome == alphanum:
            return True
        else: 
            return False
