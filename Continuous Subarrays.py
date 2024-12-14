class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        m1 , m2 = [] , []

        res = 0

        st , end = 0 , 0

        while end < len(nums):

            heapq.heappush(m1 , [-1 * nums[end] , end])

            heapq.heappush(m2 , [nums[end] , end])

            while m1 and m2 and -m1[0][0] - m2[0][0] > 2:

                # if -m1[0][0] - m2[0][0] > 2:

                st += 1

                while m1 and m1[0][1] < st:

                    heapq.heappop(m1)

                while m2 and m2[0][1] < st:

                    heapq.heappop(m2)

            res += end - st + 1

            end += 1

        return res
