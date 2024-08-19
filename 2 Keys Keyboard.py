class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0

        cnt = 0

        itr = 2

        while n > 1:

            while n % itr == 0:

                cnt += itr

                n = n // itr

            itr += 1

        return cnt