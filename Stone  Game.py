class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dp = [[0] * len(piles) for _ in range(len(piles))]

        for i in range(len(piles)):

            dp[i][i] = piles[i]

        for i in range(1 , len(piles)):

            for j in range(len(piles) - i):

                dp[j][j + i] = max(piles[j] - dp[j+1][j+i] , piles[j+i] - dp[j][j+i-1])

        return True if dp[0][-1] > 0 else False