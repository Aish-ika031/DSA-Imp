class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def even_count(num):
            
            cnt = 0
            
            while num > 0:
                
                cnt += 1
                
                num //= 10
                
            return cnt
        
        cnt = 0
        
        for i in nums:
            
            curr = even_count(i)
            
            cnt += 1 if curr % 2 == 0 else 0
            
        return cnt
        
        