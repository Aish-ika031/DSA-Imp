class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x , y , grid):

            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):

                return

            if grid[x][y] == '1':

                grid[x][y] ='0'

                dfs(x+1 , y , grid)

                dfs(x-1 , y , grid)

                dfs(x , y+1 , grid)

                dfs(x , y-1 , grid)

        res = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == '1':

                    res += 1

                    dfs(i , j , grid)

        return res
