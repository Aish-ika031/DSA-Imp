# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        # global mn_str

        # mn_str = ""

        def traverse(root , curstr):

            nonlocal mn_str

            # print(mn_str)

            if root is None:

                return 

            curstr = chr(root.val + 97) + curstr

            # print(curstr)

            if root.left == None and root.right == None:

                if mn_str == "" or curstr < mn_str:

                    mn_str = curstr

                # mn_str = min(mn_str , curstr)

            traverse(root.left , curstr)

            traverse(root.right , curstr)

            # print(mn_str)

        mn_str = ""

        traverse(root , "")

        return mn_str


        