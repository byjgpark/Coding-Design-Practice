# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the children
        # root.left, root.right = root.right, root.left
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        
        # make 2 recursive calls
        self.invertTree(root.left)
        print("check root.right", root)
        self.invertTree(root.right)
        
        print("check root at the end of function :", root)
        
        return root
