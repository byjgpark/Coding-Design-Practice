
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        max_diameter = [0]
        
        def height(node):
            if not node:
                return 0

            lheight = height(node.left)
            rheight = height(node.right)
            
            diameter = lheight + rheight

            max_diameter[0] = max(max_diameter[0], diameter)

            return 1 + max(lheight, rheight)
        
        height(root)

        print("check here", max_diameter[0])

        if max_diameter[0] < 4:
            return True
        else:
            return False

            


            

        