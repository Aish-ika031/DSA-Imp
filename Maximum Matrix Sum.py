class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m1=float("inf")
        a,c=0,0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val=(matrix[i][j])
                c=c+abs(val)
                if (val)<0:
                    a=a+1
                m1=min(m1,abs(val))
        if a%2!=0:
            m=2*m1
            return c-m
        else:
            return c
