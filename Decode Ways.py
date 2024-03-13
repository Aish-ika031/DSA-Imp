class Solution:
    def numDecodings(self, s: str) -> int:

        # if s[0]=='0':

        #     return 0
        
        dp=[0]*(len(s)+1)

        dp[0]=1

        dp[1]= 0 if s[0]=='0' else 1

        for i in range(2,len(s)+1):

            single_digit=int(s[i-1:i])

            double_digit=int(s[i-2:i])

            # double_digit=10*(ord(s[i-2])-ord('0'))+single_digit

            if single_digit>=1 and single_digit<=9:

                dp[i]=dp[i]+dp[i-1]

            if double_digit>=10 and double_digit<=26:

                dp[i]=dp[i]+dp[i-2]

        print(dp)

        return dp[len(s)]