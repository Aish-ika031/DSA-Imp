class Solution:
    def coloredCells(self, n: int) -> int:
        
        cur , cnt = 1 , 4

        for i in range(2, n+1):

            cur += cnt

            cnt += 4

        return 1 if n == 1 else cur
