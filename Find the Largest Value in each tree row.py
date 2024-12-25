# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root):

            if root is None:

                return []

            res=[]

            q1=deque([])

            q1.append(root)

            while len(q1)>0:

                curr=[]

                l=len(q1)

                for _ in range(l):

                    node=q1.popleft()

                    curr.append(node.val)

                    if node.left is not None:

                        q1.append(node.left)

                    if node.right is not None:

                        q1.append(node.right)

                res.append(max(curr))

                # curr=[]

            return res

        return bfs(root)
