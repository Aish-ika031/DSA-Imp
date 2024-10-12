class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x : (x[0],x[1]))
        
        h=[]
        
        for st,end in intervals:
            
            if len(h)>0 and st>h[0]:
                
                heapq.heappop(h)
                
            heapq.heappush(h,end)
            
        return len(h)