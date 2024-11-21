class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        res = [[0] * n for _ in range(m)]

        for i,j in guards:

            res[i][j] = 2

        for i,j in walls:

            res[i][j] = 2

        directions =[(1,0) , (0,1) , (-1,0) , (0,-1)]

        for x,y in guards:

            for a,b in directions:

                i, j = x , y

                while True:

                    i += a

                    j += b

                    if i <0 or i >= m or j <0 or j >=n or res[i][j] == 2:

                        break

                    res[i][j] = 1

        cnt = 0

        for i in res:

            cnt += i.count(0)
        
        return cnt
