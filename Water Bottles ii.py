class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        cnt = 0

        res = numBottles

        while numBottles >= numExchange:

            numBottles = numBottles - (numExchange-1)

            cnt += 1

            numExchange += 1

        return cnt + res