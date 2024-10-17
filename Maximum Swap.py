class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = list(str(num))

        for i in range(len(num)):

            if i + 1 < len(num) and num[i] < max(num[i+1:]):

                mx = max(num[i+1:])

                val = num[::-1].index(mx)

                pos = len(num) - val -1

                num[i] , num[pos] = num[pos] , num[i]

                break

        return int("".join(num))