class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for val in tokens:
            match val:
                case '+':
                    t2 = int(stack.pop())
                    t1 = int(stack.pop())
                    stack.append(t1 + t2)
                case '-':
                    t2 = int(stack.pop())
                    t1 = int(stack.pop())
                    stack.append(t1 - t2)
                case '*':
                    t2 = int(stack.pop())
                    t1 = int(stack.pop())
                    stack.append(t1 * t2)
                case '/':
                    t2 = int(stack.pop())
                    t1 = int(stack.pop())
                    stack.append(t1 / t2)
                case _:
                    stack.append(val)

        return int(stack.pop())