class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(str(s)) >2 :

            new = ""

            for i in range(len(s)-1):

                cur = int(s[i])+int(s[i+1])

                cur = cur % 10

                new = new + str(cur)

            s = new

        return True if s[0] == s[1] else False
