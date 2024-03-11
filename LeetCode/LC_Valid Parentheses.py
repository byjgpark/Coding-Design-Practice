class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # print("check c", c)
            if c in closeToOpen:
                print("check c in closeToOpen :", c)
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
