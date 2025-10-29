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
