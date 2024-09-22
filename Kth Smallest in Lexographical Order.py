class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def func(cur , n):

            nxt = cur + 1

            t_cnt = 0

            while cur <= n:

               t_cnt += nxt - cur
               
               cur *= 10
               
               nxt *= 10
               
               nxt = min(nxt , n + 1)

            return t_cnt

        cur = 1

        k -= 1

        while k > 0:

            cnt = func(cur ,n)

            if cnt <= k:

                cur += 1

                k -= cnt

            else:

                cur *= 10

                k -= 1
            # print(cur)

        return cur



            
        