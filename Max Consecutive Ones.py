class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        curr_cnt = 0

        mx_cnt = 0

        for i in range(len(nums)):

            if nums[i] == 1:

                curr_cnt += 1

                mx_cnt = max(mx_cnt , curr_cnt)

            else:

                curr_cnt = 0

        return mx_cnt

            
        