class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        for i in range(1 , len(grid[0])):

            val = 0

            for j in range(len(grid)):

                curr = grid[j][i]

                if not (curr > grid[j][i - 1] or (j > 0 and curr > grid[j - 1][i - 1]) or (j < len(grid) - 1 and curr > grid[j + 1][i - 1])):

                    grid[j][i] = float("inf")

                    val += 1

                if val == len(grid[0]):

                    return i - 1

        return len(grid[0]) - 1
        
