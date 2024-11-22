class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        map = defaultdict(int)

        # res = ""
        
        for i in matrix:

            res = ""

            for j in i:

                if i[0] == j:

                    res += "T"

                else:

                    res += "F"

            print(res)

            map[res] += 1 

        return max(map.values())
