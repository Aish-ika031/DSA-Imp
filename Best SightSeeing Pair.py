class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        mx = values[0]

        res = float("-inf")

        for i in range(1 , len(values)):

            res = max(res , mx + values[i] - i)

            mx = max(mx , values[i] + i)

        return res
