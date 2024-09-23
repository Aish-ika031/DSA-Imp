class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        d1 = set(dictionary)
        
        dp = [0] * (len(s) + 1)

        for i in range(len(s) - 1 , -1 , -1):

            dp[i] = 1 + dp[i+1]

            for j in range(i , len(s)):

                val = s[i:j + 1]

                if val in d1:

                    dp[i] =  min(dp[i] , dp[j + 1])

        return dp[0]