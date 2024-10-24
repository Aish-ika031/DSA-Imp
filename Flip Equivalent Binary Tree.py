# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def f(root1,root2):

            if root1==root2:

                return True

            if root1==None or root2==None:

                return False

            if root1.val!=root2.val:

                return False

            s1=f(root1.left,root2.left) and f(root1.right,root2.right)

            s2=f(root1.left,root2.right) and f(root1.right,root2.left)

            return s1 or s2
            
        return f(root1,root2)
            
