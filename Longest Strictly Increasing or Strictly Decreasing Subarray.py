class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        incr_len , decr_len = 1 , 1

        mx_len = 1

        for i in range(1 , len(nums)):

            if nums[i] > nums[i-1]:

                incr_len += 1
                
                decr_len = 1

            elif nums[i] < nums[i-1]:

                decr_len += 1

                incr_len = 1

            else:

                incr_len , decr_len = 1 , 1

            mx_len = max(mx_len , max(incr_len , decr_len))

        return mx_len
        