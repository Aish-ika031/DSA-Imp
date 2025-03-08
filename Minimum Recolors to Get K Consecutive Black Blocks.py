class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        mn = float("inf")

        for i in range(len(blocks) - k + 1):

            cnt = 0

            for j in range(i , i +k):

                if blocks[j] == 'W':

                    cnt  += 1

            mn = min(mn , cnt)

        return mn
