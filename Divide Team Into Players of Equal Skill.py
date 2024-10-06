class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        if len(skill)==2:
            
            return skill[0]*skill[1]
        
        skill.sort()
        
        res=0
        
        curr=skill[0]+skill[-1]
        
        for i in range(len(skill)//2):
            
            # curr=skill[i]+skill[len(skill)-i-1]
            
            if curr==skill[i]+skill[len(skill)-i-1]:
                
                res=res+skill[i]*skill[len(skill)-i-1]
                
            else:
                
                return -1
            
        return res
            