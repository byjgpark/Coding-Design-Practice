# 1st trial
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


# 2nd trial
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)

            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)

            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a*b)

            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))

            else:
                stack.append(int(token))

            # print("check stack =", stack)
            # print("Check token =", token)
        return stack[0]
                    

        