class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_partners = [("(", ")"), ("[", "]"), ("{","}")]
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            else:
                open_bracket = stack.pop()
                partner = (open_bracket, bracket)
                if partner not in valid_partners:
                    return False
        if not stack: return True
