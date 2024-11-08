class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        res = [0] * len(nums)

        val = 0

        for i in nums:

            val = val ^ i

        mx = int(2** maximumBit - 1)

        for i in range(len(nums)):

            res[i] = val ^ mx

            val = val ^ nums[len(nums) - 1 - i]

        return res
