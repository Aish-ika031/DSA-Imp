class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()

        dp=[[i] for i in nums]

        for i in range(len(nums)):

            for j in range(i):

                if nums[i]%nums[j]==0:

                    if len(dp[i])<len(dp[j])+1:

                        dp[i]=dp[j]+[nums[i]]
                        
        return max(dp,key=len)
