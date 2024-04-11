import sys
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        sys.set_int_max_str_digits(100001)

        if len(num) == k:

            return "0"

        st = []

        for i in num:

            while k > 0 and st and i < st[-1]:

                st.pop()

                k -= 1

            st.append(i)

        while k > 0 and st:

            st.pop()

            k -= 1

        return str(int("".join(st)))
        