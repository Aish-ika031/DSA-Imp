class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        d1 = {chr(i + 96) : i for i in range(1 , 27)}

        res = ""

        for i in s:

            res = res + str(d1[i])

        print(res)

        final = 0

        while k > 0:

            final = 0

            for i in res:

                final += int(i)

                # print(final)

            res = str(final)

            k -= 1

        return int(final)


