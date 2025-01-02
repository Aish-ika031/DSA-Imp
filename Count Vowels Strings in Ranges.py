class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        [1,0,1,1,1]
        
        [1,1,2,3,4]
        
        vowel=['a','e','i','o','u']
        
        prefix=[]
        
        for i in range(len(words)):
            
            curr=words[i]
            
            if curr[0] in vowel and curr[-1] in vowel:
                
                prefix.append(1)
                
            else:
                
                prefix.append(0)
                
        res=[0]*(len(prefix)+1)
        
        res[0]=prefix[0]
        
        for i in range(1,len(prefix)):
            
            res[i]=res[i-1]+prefix[i]
            
        print(res)
        
        result=[]
        
        for i in queries:
            
            st,end=i[0],i[1]
            
            result.append(res[end]-res[st-1])
                
        return result
