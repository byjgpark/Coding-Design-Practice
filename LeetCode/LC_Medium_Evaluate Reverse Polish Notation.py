# tokens = ["2", "1", "+", "3", "*"]

# tokens = ["3", "3", "*"]

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         while len(tokens) > 1:
#             for i in range(len(tokens)):
#                 if tokens[i] in "+-*/":
#                     a = int(tokens[i-2])
#                     b = int(tokens[i-1])
#                     if tokens[i] == '+':
#                         result = a + b
#                     elif tokens[i] == '-':
#                         result = a - b
#                     elif tokens[i] == '*':
#                         result = a * b
#                     elif tokens[i] == '/':
#                         result = int(a / b)
#                     tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
#                     break
#         return int(tokens[0])

# ## whats its time and space compelxity?
# ## time: O(n)
# ## space: O(n)

# 2nd trial 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        print("check tokens =", tokens)

        print("check tokens =", len(tokens))

        while len(tokens) > 1:
            for i in range(tokens):
                if tokens[i] == "+":


# 3rd trial
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        print("check tokens =", tokens)

        print("check tokens =", len(tokens))

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    # print("check tokens[i] =", tokens[i], " check i= ",i)
                    a=int(tokens[i-2])
                    # b=int(tokens[i-2])
                    b=int(tokens[i-1])
                    print("check a =",a ," b =",b)

# 4th trial
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        print("check tokens =", len(tokens))

        result = 0
        operators = {"+", "-", "*", "/"}

        while len(tokens) > 1:
            for i in range(len(tokens)):
                # print("check i =",i)
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == "+" in tokens:
                        result = a+b
                        print("check result", result) 

                    elif tokens[i] == "*" in tokens: 
                        result = a*b 
                        print("check tokens", i)

                    elif tokens[i] == "-" in tokens: 
                        result = a-b 
                        print("check tokens", i)

                    elif tokens[i] == "/" in tokens: 
                        result = a/b 
                        print("check tokens", i)

# 5th trial
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        i = 2
        # first = tokens[:i-2]
        # second = tokens[i+1:]
        res=0
        # print("Check first =", first, " second =", second)

        while len(tokens)>1:
            for i in range(len(tokens)):
                # print("Check i =", i) 
                if tokens[i] in "+-*/":
                    a=int(tokens[i-2])
                    b=int(tokens[i-1])
                    if tokens[i] == "+":
                        res=a+b
                    elif tokens[i] == "-":
                        res=a-b
                    elif tokens[i] == "*":
                        res=a*b
                    elif tokens[i] == "/":
                        res=int(a/b)
                        # print("check res =",res)
                        # print("check abs(a//b) =", abs(a//b))
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    # print("Check tokens =", tokens)
                    break

        return int(tokens[0])
                    
            

                

        

        