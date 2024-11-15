class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        st ,end = 1 , max(quantities)

        # s= 0

        while st < end :

            mid = (st + end) // 2

            s = 0

            for i in quantities:

                s = s + ceil(i / mid)

            if s <= n :

                end = mid

            else:

                st = mid + 1

        return st

