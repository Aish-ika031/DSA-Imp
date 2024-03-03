class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for i in nums:
            
            heap.append(1*i)
            
        heapq.heapify(heap)
        
        cnt = 0
        
        while len(heap) > 0 and heap[0] < k:
            
            a , b = heapq.heappop(heap) , heapq.heappop(heap)
            
            print(a ,b)
            
            heapq.heappush(heap , 2*a + b)
            
            cnt += 1
            
        return cnt