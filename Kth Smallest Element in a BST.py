# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def traversal(root , res):

            if root is None:

                return 

            traversal(root.left , res)

            res.append(root.val)

            traversal(root.right , res)

            return res

        res = traversal(root , [])

        heapq.heapify(res)

        st = 0

        while st != k:

            cur = heapq.heappop(res)

            st += 1

        return cur


        