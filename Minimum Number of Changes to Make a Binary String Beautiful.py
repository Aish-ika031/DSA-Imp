class Solution:
    def minChanges(self, s: str) -> int:
        
        if s.count('0')==len(s) or s.count('1')==len(s):
            
            return 0
        
        cnt=0
        
        for i in range(0,len(s)-1,2):
            
            if s[i]!=s[i+1]:
                
                cnt=cnt+1
                
                
                
        return cnt
