class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort(reverse = True)
        
        total_cnt = sum(apple)
        
        cur , cnt = 0 , 0
        
        for i in capacity:
            
            cur += i
            
            cnt += 1
            
            if cur >= total_cnt:
                
                return cnt
            
        
                
                
            
            