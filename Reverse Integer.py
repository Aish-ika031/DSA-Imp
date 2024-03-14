class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:

            val = int(str(x)[::-1])

            if val >= -1 * 2**31-1 and val <= 2**31 -1 :

                return int(str(x)[::-1])

            else:

                return 0

        else:

            val = -1 * int((str(x))[::-1][:-1])

            if val >= -1*2**31-1 and val <= 2**31-1:

                return val

            return 0

            

        # return int(str(x)[::-1]) if x >=0 and int(str(x)[::-1]) < = 2**31 -1   else -1 * int((str(x))[::-1][:-1])