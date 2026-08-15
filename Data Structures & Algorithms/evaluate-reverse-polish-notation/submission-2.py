class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        operators = ["+", "-", "*", "/"]
        result = tokens[0]
        for token in tokens[1:]: 
            print(result)
            if token in operators:
                match (token) :
                    
                    case "+": result = result + op_stack.pop()
                    case "-": result = result - op_stack.pop()
                    case "*": result = result * op_stack.pop()
                    case "/": result = result / op_stack.pop()
                
            else:
                op_stack.append(token)
        return result