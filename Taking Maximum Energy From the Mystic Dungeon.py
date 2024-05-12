class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        dp = [0] * len(energy)

        mx = float("-inf")

        for i in range(len(energy) -1 , -1 , -1):

            if i + k < len(energy):

                 dp[i] = dp[i+k] + energy[i]

            else:

                dp[i] = energy[i]

            # print(dp)

            mx = max(mx , dp[i])

        return mx