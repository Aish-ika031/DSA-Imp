from collections import Counter
class Solution:

    def check(self,d1,d2):

        for i in range(97,123):

            if d1[chr(i)]!=d2[chr(i)]:

                return False

        return True


    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        mp1={chr(i):0 for i in range(97,123)}

        for i in range(len(s1)):

            mp1[s1[i]]=mp1[s1[i]]+1

        mp2={chr(i):0 for i in range(97,123)}

        i,st=0,0

        while i<len(s2) and st<len(s2):

            mp2[s2[i]]=mp2[s2[i]]+1

            print(mp2)
            
            if i-st+1==len(s1) and self.check(mp1,mp2):
               
               return True
               
            elif i-st+1<len(s1):

                i=i+1

            else:
                
                mp2[s2[st]]-=1

                st=st+1

                i=i+1

        return False

               