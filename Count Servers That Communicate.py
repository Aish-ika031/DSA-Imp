class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        v1 , v2 = [0] * len(grid) , [0] * len(grid[0])

        cnt = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:

                    v1[i] += 1

                    v2[j] += 1

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:

                    if v1[i] >1 or v2[j] > 1:

                        cnt += 1

        return cnt
