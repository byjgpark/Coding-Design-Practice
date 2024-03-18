class Solution:
    def isValid(self, s: str) -> bool:
        closeToChar = {")":"(", "}":"{", "]":"[" }
        stack = []

        for c in s:
            if c in closeToChar:
                if stack and stack[-1] == closeToChar[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 
        

