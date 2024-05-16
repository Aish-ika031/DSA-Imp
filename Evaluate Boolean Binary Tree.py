# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            
            if root is None:
                return 
            
            if root.val==1:
                return True
            
            elif root.val==0:
                return False
            
            if root.val==2:
                return traverse(root.left) or traverse(root.right)
            
            elif root.val==3:
                return traverse(root.left) and traverse(root.right)
            
        return traverse(root)