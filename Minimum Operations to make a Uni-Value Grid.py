class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        rem = grid[0][0] % x

        res = []

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] % x != rem:

                    return -1

                res.append(grid[i][j])

        res.sort()

        median = len(res) // 2

        print(median)

        cnt = 0

        for i in range(len(res)):

            # print(abs(res[i] - res[median]))

            cnt += abs(res[i] - res[median]) // x

            print(cnt)

        return cnt
