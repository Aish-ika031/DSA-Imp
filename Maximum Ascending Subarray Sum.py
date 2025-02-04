class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        cur = nums[0]

        mx = 0

        for i in range(1, len(nums)):

            if nums[i] <= nums[i-1]:

                mx = max(mx , cur)

                cur = 0

            cur += nums[i]

        return max(mx , cur)
