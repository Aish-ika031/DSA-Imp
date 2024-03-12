# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def check(root,p,q):

            if root is None:

                return None

            if root.val==p.val or root.val==q.val:

                return root

            l=check(root.left,p,q)

            r=check(root.right,p,q)

            if l is not None and r is not None:

                return root

            if l is not None:

                return l

            else:

                return r

        return check(root,p,q)
                
        