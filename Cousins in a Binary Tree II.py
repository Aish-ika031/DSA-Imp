# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def bfs(root):

            if root is None:

                return root

            q1 = deque()

            q1.append(root)

            prev = root.val

            while len(q1) > 0:

                l = len(q1)

                curr = 0

                # s = 0

                for _ in range(l):

                    node = q1.popleft()

                    node.val = prev - node.val

                    s = 0
                    

                    if node.left is not None:

                        s += node.left.val

                    if node.right is not None:

                        s += node.right.val

                    if node.left is not None:

                        curr += node.left.val

                        node.left.val = s

                        q1.append(node.left)

                    if node.right is not None:

                        curr += node.right.val

                        node.right.val = s

                        q1.append(node.right)

                prev = curr

                # print(root)

            return root

        return bfs(root)
