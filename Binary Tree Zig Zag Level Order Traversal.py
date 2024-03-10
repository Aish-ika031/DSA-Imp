# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(root):

            res = []

            status = True

            if root is None:

                return res

            q1 = deque([])

            q1.append(root)

            while len(q1)>0:

                print(len(q1))

                curr_level = deque([])

                l = len(q1)

                for i in range(0 , l):

                    node = q1.popleft()

                    # print(node)

                    if status:

                        curr_level.append(node.val)

                    else:

                        curr_level.appendleft(node.val)

                    if node.left is not None:

                        q1.append(node.left)

                    if node.right is not None:

                        q1.append(node.right)

                status = not status

                print(res)

                res.append(curr_level)

            return res

        return bfs(root)
