class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        c1 , c2 = {} , {}

        cnt = 0

        for i in range(len(s)):

            if s[i] not in c1:

                c1[s[i]] = cnt

            if t[i] not in c2:

                c2[t[i]] = cnt

            cnt += 1

        for i in range(len(s)):

            if c1[s[i]] != c2[t[i]]:

                return False

        return True