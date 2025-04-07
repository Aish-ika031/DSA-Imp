class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1=sum(nums)

        n=len(nums)
        
        if s1%2!=0:
        
            return False
        
        else:
        
            s2=s1//2
        
            dp=[[False for x in range(s2 + 1)]for x in range(n + 1)]
            ##for i in range(n+1):
                ##dp[i][0]=True
        
            for i in range(0,n+1):
        
                for j in range(0,s2+1):
        
                    if i==0:
        
                        dp[i][0]=True
        
                    elif nums[i-1]>j:
        
                        dp[i][j]=dp[i-1][j]
        
                    else:
        
                        dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
            return dp[len(nums)][s2]
