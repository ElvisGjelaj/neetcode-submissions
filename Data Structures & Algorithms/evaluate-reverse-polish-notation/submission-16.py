class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens: 
            if token in operators:
                b = op_stack.pop()
                a = op_stack.pop()
                match (token) :
                    case "+": result = a + b
                    case "-": result = a - b
                    case "*": result = a * b
                    case "/": result = int(a / b)
                op_stack.append(result) 
            else:
                op_stack.append(int(token))
                
        return op_stack[0]