class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []

        cnt = 1

        for i in range(n):

            res.append(cnt)

            if cnt * 10 <= n:

                cnt *= 10
            
            else:

                while cnt % 10 == 9 or cnt + 1 > n:

                    cnt //= 10

                cnt += 1

        return res

        