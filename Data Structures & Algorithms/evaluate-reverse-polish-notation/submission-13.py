class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens: 
            if token in operators:
                match (token) :
                    case "+": result = op_stack.pop() + op_stack.pop()
                    case "-": result = op_stack.pop() - op_stack.pop()
                    case "*": result = op_stack.pop() * op_stack.pop()
                    case "/": result = op_stack.pop() / op_stack.pop()

                op_stack.append(result)
                
            else:
                op_stack.append(int(token))
        print(result)
        return op_stack[0]