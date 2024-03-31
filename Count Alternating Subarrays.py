class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:

        cnt = 0

        idx = -1

        for i in range(1 , len(nums)):

            if nums[i] == nums[i-1]:

                idx = (i-1)

            cnt += i - idx

        return cnt + 1
        