class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        neighbour , cell = 0 , 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:

                    cell += 1

                    if i-1 >=0 and grid[i-1][j] == 1:

                        neighbour += 1

                    if j-1 >= 0 and grid[i][j-1] == 1:

                        neighbour += 1

        return 4*cell - 2*neighbour