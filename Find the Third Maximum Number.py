class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = list(set(nums))

        if len(nums) <= 2:

            return max(nums)

        mx_heap = []

        for i in nums:

            mx_heap.append(-1*i)

        heapify(mx_heap)

        cnt = 3

        while cnt != 0:

            val = heapq.heappop(mx_heap)

            cnt = cnt -1

        return -1*val
        