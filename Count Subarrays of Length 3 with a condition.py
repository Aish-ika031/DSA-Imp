class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        cnt = 0
        
        for i in range(1 , len(nums)-1):

            if (nums[i-1] + nums[i+1]) * 2 == nums[i]:

                cnt += 1

        return cnt
