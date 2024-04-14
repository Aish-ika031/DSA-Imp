# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def traverse(root):

            if root is None:

                return 0

            res = 0

            if root.left:

                if root.left.left == None and root.left.right == None:

                    res += root.left.val

                else:

                    res += traverse(root.left)

            res += traverse(root.right)

            return res

        return traverse(root)
        