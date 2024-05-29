class Solution:
    def numSteps(self, s: str) -> int:
        
        decimal = int(s , 2)

        cnt = 0

        while decimal > 1:

            if decimal % 2 == 0:

                decimal = decimal // 2

            else:

                decimal += 1

            cnt += 1

        return cnt