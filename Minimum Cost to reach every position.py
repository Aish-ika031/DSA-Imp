class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        
        res = [float("inf")]* len(cost)

        for i in range(len(cost)):

            res[i] = cost[i]

            if i> 0:

                res[i] = min(res[i - 1] , res[i])

        return res
