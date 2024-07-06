
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # max_diameter = [0]
        Flag = [True]
        
        def height(node):
            if not node:
                return 0

            lheight = height(node.left)
            rheight = height(node.right)

            print("lheight", lheight,"rheight", rheight)
            
            abs_value = abs(lheight - rheight)

            print("check abs_value", abs_value)

            if abs_value > 1:
                print("checking here")
                Flag[0] = False
            # else:
            #     return False

            # max_diameter[0] = max(max_diameter[0], diameter)

            return 1 + max(lheight, rheight)
        
        print("check here",height(root))
        return Flag[0]

        # return True
        

        # print("check here", max_diameter[0])

        # if max_diameter[0] < 4:
        #     return True
        # else:
        #     return False

            


            

        