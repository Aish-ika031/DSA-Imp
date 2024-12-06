class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        # res=[i for i in range(1,n+1)]

        banned=set(banned)
        
        # for i in banned:
            
        #     if i in res:
                
        #         res.remove(i)
                
        # # print(res)    
                
        curr_sum=0
        
        cnt=0
        
        # if sum(res)<=maxSum:
            
        #     return len(res)
        
        for i in range(1,n+1):
            
            if i not in banned and curr_sum+i>maxSum:
                
                break

            if i not in banned and curr_sum+i<=maxSum:
                
                curr_sum=curr_sum+i
                
                cnt=cnt+1
                
        return cnt
