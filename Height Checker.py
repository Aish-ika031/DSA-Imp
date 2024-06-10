class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        h=sorted(heights)
        
        cnt=0
        
        for i in range(len(h)):
            
            if h[i]!=heights[i]:
                
                cnt=cnt+1
        
        return cnt
        