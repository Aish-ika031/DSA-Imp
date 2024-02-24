class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        
        st.append(["", 1])
        
        curr = ""
        
        for i in s:
            
            if i.isdigit():
                
                curr=curr+i
                
            elif i=='[':
                
                st.append(["", int(curr)])
                
                curr = ""
                
            elif i==']':
                
                a,b= st.pop()
                    
                st[-1][0]=st[-1][0]+(a*b)
                
            else:
                
                st[-1][0]=st[-1][0]+i
                
        return st[0][0]