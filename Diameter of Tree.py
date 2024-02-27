# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.mx = 0

        def dfs(root):

            if root is None:

                return 0

            l , r = dfs(root.left) , dfs(root.right)

            self.mx = max(self.mx , (l + r))

            return 1 + max(l , r)

        dfs(root)

        return self.mx
        