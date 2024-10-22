# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        heap =[]

        q1 = deque()

        q1.append(root)

        while len(q1) > 0:

            l = len(q1)

            curr_sum = 0

            for _ in range(l):

                node = q1.popleft()

                curr_sum += node.val

                if node.left:

                    q1.append(node.left)

                if node.right:

                    q1.append(node.right)

            heapq.heappush(heap , -1 * curr_sum)

        if len(heap) < k:

            return -1

        for i in range(k):

            if i == k - 1:

                return -1 * heapq.heappop(heap)

            heapq.heappop(heap)       
