class Solution:
    def getSmallestString(self, s: str) -> str:
        
        s = list(s)

        for i in range(len(s) - 1):

            if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0 or (int(s[i]) % 2 != 0 and int(s[i+1]) % 2 
            != 0):

                if int(s[i]) > int(s[i+1]):

                    s[i] , s[i+1] = s[i+1] , s[i]

                    break

        return "".join(s)