# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        longest_diameter = [0]

        def height(node):
        
            if not root:
                return 0
        
            lheight = height(node.left)
            rheight = height(node.right)
            
            diamter = lheight + rheight
            
            longest_diameter[0] = max(longest_diameter[0], diamter)
            
            return 1 + max(lheight+rheight)

        height(root)
        
        return longest_diameter[0]
        


            
        
