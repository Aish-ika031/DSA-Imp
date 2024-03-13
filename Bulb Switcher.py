class Solution:
    def bulbSwitch(self, n: int) -> int:

        cnt= 0

        for i in range(1,int(sqrt(n))+1):

            cnt += 1

        return cnt
        