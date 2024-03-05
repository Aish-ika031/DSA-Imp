class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        mx = 0
        
        for i in accounts:

            mx = max(mx , sum(i))

        return mx