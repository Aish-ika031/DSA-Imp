class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        mn = float("inf")

        for i in range(len(nums) - l + 1):

            for j in range(l , r + 1):

                cur = sum(nums[i:i+j])

                mn = min(mn , cur) if cur > 0 else mn

        return -1 if mn == float("inf") else mn
