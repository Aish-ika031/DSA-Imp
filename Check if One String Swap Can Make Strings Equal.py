class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        cnt  =0

        s1_new , s2_new = set() , set()
        
        for i in range(len(s1)):

            if s1[i]  != s2[i]:

                cnt += 1

                s1_new.add(s1[i])

                s2_new.add(s2[i])

            if cnt > 2:

                return False

        if cnt ==2 and s1_new == s2_new:

            return True

        elif cnt == 0:

            return True

        else:

            return False
