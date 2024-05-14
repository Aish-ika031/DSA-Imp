class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def recur(st,end):
            
            if st==0 and end==0:
                return 1
            #reached start of the grid 
            
            if st<0 or end<0:
                return 0
            #when exceed the boundaries of left and down 
            
            #if we start from bottom we can move upwards or left
            #upwards -> row -1 ,col=same
            #left -> row=same,col-1
            
            up=recur(st-1,end)
            
            left=recur(st,end-1)
            
            return up+left
        
        #Time complexity : 2^(m*n) (as every index has 2 options up or left if we start from last end of matrix)
        #Space complexity : Path Length = (m-1)+(n-1)
        
        def memoize(st,end):
            dp=[[-1 for _ in range(end+1)] for _ in range(st+1)]
            
            if st==0 and end==0:
                return 1
            
            if st<0 or end <0:
                return 0
            
            if dp[st][end]!=-1:
                return dp[st][end]
            
            up=recur(st-1,end)
            
            left=recur(st,end-1)
            
        #Time complexity : O(m*n)
        #S.C. : O((m-1)+(n-1))  + O(m*n)
        
        def tabulation(st,end):
            
            dp=[[1 for _ in range(end+1)] for _ in range(st+1)]
            
            # dp[0][0]=1
            
            for i in range(1,st):
                
                for j in range(1,end):
                    
#                     if i==0 and j==0:
#                         dp[0][0]=1
                        
#                     elif i>0 and j>0:
                        
                        # up=dp[i-1][j] 
                        # left=dp[i][j-1] 
                        
                        # dp[i][j]=up+left
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                    
            #print(dp)
                    
            return dp[st-1][end-1]
        
        return tabulation(m,n)