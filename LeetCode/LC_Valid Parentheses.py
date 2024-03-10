class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # if c not in Map:
            #     stack.append(c)
            #     continue
            if not stack or stack[-1] != Map[c]:
                print("check here")
            
        #         return False
        #     stack.pop()
            # print("check here :", not stack != Map.get(c, None))

        # return not stack
