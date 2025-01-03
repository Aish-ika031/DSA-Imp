class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        t_sum=sum(nums)
        
        curr_sum=0
        
        cnt=0
        
        for i in range(len(nums)-1):
            
            curr_sum=curr_sum+nums[i]
            
            rem_sum=t_sum-curr_sum
            
            if curr_sum >= rem_sum:
                
                #print(curr_sum,rem_sum)
                
                cnt=cnt+1
                
        return cnt
