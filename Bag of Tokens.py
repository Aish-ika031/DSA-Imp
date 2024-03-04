class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        st,end=0,len(tokens)-1
        
        cnt,mx=0,0
        
        while st<=end:
            
            if tokens[st]<=power:
                
                cnt=cnt+1
                
                power=power-tokens[st]
                
                st=st+1
                
            else:
                
                if cnt>=1:
                
                    power=power+tokens[end]

                    end=end-1

                    cnt=cnt-1
                    
                else:
                    
                    break
                    

            mx=max(mx,cnt)
            
            # print(cnt,mx)
            
            
            
        return mx