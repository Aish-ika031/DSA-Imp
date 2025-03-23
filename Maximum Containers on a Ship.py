class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:

        total = n * n

        cnt = maxWeight // w

        return min(n*n , cnt)

