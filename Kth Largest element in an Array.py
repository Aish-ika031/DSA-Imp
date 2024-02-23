class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        mx_heap = []

        for i in nums:

            mx_heap.append(-1*i)

        heapq.heapify(mx_heap)

        while k!=0:

            val = heapq.heappop(mx_heap)

            k=k-1

        return -1*val