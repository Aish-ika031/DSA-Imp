# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traversal(root  , res):

            if root is None:

                return 

            traversal(root.left , res)

            res.append(root.val)

            traversal(root.right , res)

            return res

        return traversal(root , [])