class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        cur1 , cur2 = sum(grid[0]) , 0

        mn = 9999999999

        for i in range(len(grid[0])):

            cur1 -= grid[0][i]

            val = max(cur1 , cur2)

            mn = min(mn , val)

            cur2 += grid[1][i]

        return mn
