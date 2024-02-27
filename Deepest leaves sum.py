# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):

            q1 = deque()

            q1.append(root)

            while q1:

                n = len(q1)

                curr = 0

                for i in range(n):

                    node = q1.popleft()

                    curr += node.val

                    if node.left:

                        q1.append(node.left)

                    if node.right:

                        q1.append(node.right)

            return curr

        return bfs(root)