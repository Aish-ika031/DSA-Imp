class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        val = pow(len(grid) , 2)
        
        res = [i for i in range(1,val + 1)]

        mat = []

        ans = []

        for i in range(len(grid)):

            for j in range(len(grid)):

                mat.append(grid[i][j])

        for i in res:

            if mat.count(i) > 1:

                ans.append(i)

        for i in res:

            if i not in mat:

                ans.append(i)

        return ans
