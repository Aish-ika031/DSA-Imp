class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        cnt = 0

        for i in range(len(nums)):

            if nums[i] == 0 and i + 2 < len(nums):

                nums[i] = 1

                nums[i+1] = 1 - nums[i+1]

                nums[i+2] = 1 - nums[i+2]

                cnt += 1

        for i in range(len(nums)):

            if nums[i] == 0:

                return -1

        return  cnt