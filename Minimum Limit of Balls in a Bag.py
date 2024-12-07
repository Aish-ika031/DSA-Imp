class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        st , end = 1 , max(nums)

        # cur = 0

        while st < end:

            mid = (st + end ) // 2

            cur = 0

            for i in nums:

                cur += (i-1) //mid

            if cur <= maxOperations:

                end = mid

            else:

                st = mid + 1


        return end
