# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(root , status):

            if root is None:

                return None

            ispresent = True if root.val in s else False

            root.left = dfs(root.left , ispresent)

            root.right = dfs(root.right , ispresent)

            if not ispresent and status:

                res.append(root)

            if ispresent:

                return None

            else:

                return root

        s = set(to_delete)

        res = []

        dfs(root , True)

        return res

        