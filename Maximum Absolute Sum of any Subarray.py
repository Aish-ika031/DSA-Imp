class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        m1 , m2 = 0 , 0

        cur_sum = 0

        for i in range(len(nums)):

            cur_sum += nums[i]

            m1 = min(m1 , cur_sum)

            m2 = max(m2 , cur_sum)

        val = m2 - m1

        return val
