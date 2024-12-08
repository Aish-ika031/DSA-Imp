class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        heap = []

        mx , cur = 0 , 0

        events.sort(key=lambda val : val[0])

        for i in events:

            while len(heap) > 0 and heap[0][0] < i[0]:

                cur = max(cur , heap[0][1])

                heapq.heappop(heap)

            mx = max(mx , cur + i[2])

            heapq.heappush(heap , [i[1] , i[2]])

        return mx
