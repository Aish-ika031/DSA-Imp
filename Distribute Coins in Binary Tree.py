# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.cnt = 0
        
        def dfs(root):

            cnt = 0

            if root == None:

                return 0

            l , r = dfs(root.left) , dfs(root.right)

            self.cnt += abs(l) + abs(r)

            return root.val - 1 + l + r

        dfs(root)

        return self.cnt