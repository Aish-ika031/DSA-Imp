class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        # if len(nums) == 2:

        #     return nums[0] - nums[1]
        
        mn_diff = float("-inf")

        for i in range(len(nums)):

            diff = abs(nums[i] - nums[(i+1)%len(nums)])

            mn_diff = max(mn_diff , diff)

        return mn_diff
