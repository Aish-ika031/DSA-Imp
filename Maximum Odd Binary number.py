class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        cnt_one = s.count('1')

        cnt_zero = s.count('0')

        res = (cnt_one - 1) * '1' + cnt_zero * '0' + '1'

        return res


        