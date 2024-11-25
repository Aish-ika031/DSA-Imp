class Solution:
    def canAliceWin(self, n: int) -> bool:

        cnt = 1

        prev = 10

        if n >= 10:

            n = n - prev

        else:

            return False
        
        while True:

            prev = prev -1 

            if n >= prev :

                n = n - prev

            else:

                break

            cnt += 1 

        return True if cnt % 2 else False
