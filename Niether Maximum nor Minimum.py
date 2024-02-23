class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            if nums[i] != max(nums) and nums[i] != min(nums):

                return nums[i]

        return -1
        