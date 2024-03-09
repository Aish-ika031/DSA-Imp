# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traversal(root , res):

            if root is None:

                return 

            traversal(root.left , res)

            traversal(root.right , res)

            res.append(root.val)

            return res

        return traversal(root , [])
        