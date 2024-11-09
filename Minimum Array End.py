class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        x1 , n1 = 0 ,0 

        cnt = x

        n = n - 1

        while n >> n1:

            if x & ( 1 << x1):

                x1 += 1

                continue

            val = n >> n1 & 1

            cnt = cnt | val << x1

            x1 += 1

            n1 += 1

        return cnt
