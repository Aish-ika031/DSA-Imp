class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        heap = []
        
        for i in happiness:
            
            heapq.heappush(heap , -1*i)
            
        res = 0
        
        st = 0
            
        while k!=0:
            
            cur = -1 * heapq.heappop(heap) - st
            
#             for i in heap:
                
#                 heapq.heappush(heap , -1*i-1)
                
#             # print(cur)
                
            res += cur if cur > 0 else 0
            
            k -= 1
            
            st += 1
            
        return res