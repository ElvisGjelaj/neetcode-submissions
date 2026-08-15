class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        operators = ["+", "-", "*", "/"]
        result = min(tokens[0])
        for token in tokens[1:]: 
            if token in operators:
                match (token) :
                    case "+": result = result + op_stack.pop()
                    case "-": result = result - op_stack.pop()
                    case "*": result = result * op_stack.pop()
                    case "/": result = result / op_stack.pop()
                
            else:
                op_stack.append(int(token))
        return result