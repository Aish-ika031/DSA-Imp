class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        cnt=Counter(arr1)
        
        res=[]
        
        for i in range(len(arr2)):
            
            val=arr2[i]
            
            st=0
            
            while cnt[val]!=0:
                
                res.append(val)
                
                cnt[val]=cnt[val]-1
                
        rem=[]
        
        for i in cnt:
            
            if cnt[i]!=0:
                
                while cnt[i]!=0:
                    
                    rem.append(i)
                    
                    cnt[i]=cnt[i]-1
                    
        rem.sort()
        
        res.extend(rem)
        
        return res