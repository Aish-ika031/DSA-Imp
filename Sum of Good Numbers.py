class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        
        res = 0

        for i in range(len(nums)):

            if i -k >= 0 and nums[i] <= nums[i-k] or  i+k < len(nums) and nums[i] <= nums[i+k]:

                continue

            else:

                res += nums[i]

        return res

