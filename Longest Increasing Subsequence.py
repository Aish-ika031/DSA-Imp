class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def recur(indx,prev_indx,a):
            
            n=len(a)
            
            if indx == n:
                return 0
            
            l=0+recur(indx+1,prev_indx,a) #Not-Take
            
            if prev_indx==-1 or a[indx]>a[prev_indx]:
                
                l=max(l,1+recur(indx+1,indx,a)) #Take
                
            return l
        
        #T.C. = O(2*n)
        #S.C. = O(n) auxillary stack space
        
        # return recur(0,-1,nums)
        
        def memoize(indx,prev_indx,a,dp):
            
            n=len(a)
            
            if indx == n:
                return 0
            
            if dp[indx][prev_indx+1]!=-1:
                return dp[indx][prev_indx+1]
            
            l=0+memoize(indx+1,prev_indx,a,dp) #Not-Take
            
            if prev_indx==-1 or a[indx]>a[prev_indx]:
                
                l=max(l,1+memoize(indx+1,indx,a,dp)) #Take
                
            dp[indx][prev_indx+1]=l
                
            return l
        
        #T.C. = O(N*N)
        #S.C. = O(N*N) + O(N) 
        
        # dp=[[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        
        # return memoize(0,-1,nums,dp)
        
#         def tabulate(indx,prev_indx,a):
            
#             n=len(a)
            
#             dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
            
#             for i in range(n-1,1,-1):
                
#                 for j in range(i-1,0,-1):
                    
#                     l1=0+dp[i+1][j+1]
                    
#                     l2=0
                    
#                     if j==-1 or a[i]>a[j]:
                        
#                         l2=1+dp[i+1][i+1]
                        
#                 dp[i][j+1]=max(l1,l2)
                    
#             print(dp)
                    
#             # return max(dp)
        
        
        # return tabulate(0,-1,nums)
        
        dp=[1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
            
            for j in range(0,i):
                
                if nums[i]>nums[j]:
                    
                    dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
            
        return max(dp)
                    
                    