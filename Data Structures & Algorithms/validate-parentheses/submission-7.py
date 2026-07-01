class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partner = {")": "(", "}": "{", "]": "["}
        for bracket in s:
            if bracket in partner:
                if stack and stack[-1] == partner[bracket]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False

