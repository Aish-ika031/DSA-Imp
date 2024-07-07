class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        cnt = 0

        while numBottles >= numExchange:

            cnt += numExchange

            numBottles -= numExchange

            numBottles += 1

        return numBottles + cnt