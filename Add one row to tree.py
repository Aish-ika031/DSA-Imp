# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def bfs(root , val , d1):

            if d1 == 1:

                return TreeNode(val , root , None)

            q1 = deque([])

            q1.append(root)

            d1 = d1 - 1

            while d1 > 0:

                n = len(q1)

                d1 = d1 - 1

                for i in range(n):

                    node = q1.popleft()

                    nl , nr = node.left , node.right

                    if d1 == 0:

                        node.left = TreeNode(val , nl , None)

                        node.right = TreeNode(val , None , nr)

                    if nl:

                        q1.append(nl)

                    if nr:

                        q1.append(nr)

            return root

        return bfs(root , val ,depth)






        