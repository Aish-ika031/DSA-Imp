import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        h1=[]

        for i in gifts:

            heapq.heappush(h1 , -1*i)

        while k != 0:

            val = heapq.heappop(h1)

            rem = math.sqrt(-1 * val)

            heapq.heappush(h1 , int(-1*rem))

            k -= 1

        return -1*sum(h1)
