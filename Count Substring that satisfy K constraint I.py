class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        cnt = 0
        
        for i in range(len(s)):

            a , b = 0 , 0

            for j in range(i , len(s)):

                if s[j] == '0':

                    a += 1

                else:

                    b += 1

                if a <= k or b <= k:

                    cnt += 1

        return cnt