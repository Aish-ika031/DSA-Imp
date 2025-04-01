class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def solve(ques , pos , dp):

            if pos >= len(ques):

                return 0

            if dp[pos]  != -1:

                return dp[pos]

            include = solve(ques , pos + 1 , dp)

            exclude = ques[pos][0] + solve(ques , pos + ques[pos][1] + 1 , dp)

            dp[pos] = max(include , exclude)

            return dp[pos]

        res = [-1] * len(questions)

        return solve(questions , 0 , res)

