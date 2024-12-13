class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        res = 0

        h1= []

        for i in range(len(nums)):

            heapq.heappush(h1,[nums[i] ,i])

        visited = [0] * len(nums)

        while len(h1) > 0:

            cur = heapq.heappop(h1)

            if visited[cur[1]] == 0:

                res += cur[0]

                visited[cur[1]] = 1

                if cur[1] - 1 >=0:

                    visited[cur[1] - 1] = 1

                if cur[1] + 1 < len(nums):

                    visited[cur[1] + 1] = 1

        return res
