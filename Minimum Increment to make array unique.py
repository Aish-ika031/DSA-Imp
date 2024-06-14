class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        min_incr = 0

        nums.sort()

        for i in range(1 , len(nums)):

            if nums[i] <= nums[i-1]:

                cnt = nums[i-1] - nums[i] + 1

                min_incr += cnt

                nums[i] = nums[i-1] + 1

        return min_incr