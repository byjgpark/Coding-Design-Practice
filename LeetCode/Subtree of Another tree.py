# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root: 
            return False
        

        if self.sameTree(root, subRoot):
            return True
        return ( self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) )
    


    def sameTree(self, lTree, rTree) -> bool:

        if not lTree and not rTree:
            return True 
        if lTree and rTree and lTree.val == rTree.val:
            return ( self.sameTree(lTree.left, rTree.left) and self.sameTree(lTree.right,rTree.right))
        return False
