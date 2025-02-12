class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def digit_sum(n):
            
            t_sum=0
            
            while n>0:
                
                t_sum=t_sum+n%10
                
                n=n//10
                
            return t_sum
        
        d1={}
        
        for i in nums:
            
            val=digit_sum(i)
            
            if val not in d1:
                
                d1[val]=[i]
                
            else:
                
                d1[val].append(i)
                
        #print(d1)
        
        curr_sum=-1
        
        mx=-1
        
        for i in d1:
            
            l=d1[i]
            
            l.sort()
            
            if len(l)>=2:
                
                curr_sum=l[-1]+l[-2]
                
            mx=max(mx,curr_sum)
        
        return mx
            
