class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        def binary_search(n , nums , val):

            st , end = 0 , n - 1

            idx = len(nums)

            while st <= end:

                mid = (st + end) // 2

                if nums[mid] >= val:

                    idx = mid

                    end -= 1

                else:

                    st += 1

            return idx

        nums.sort()

        for i in range(1 , len(nums) + 1):

            nxt = binary_search(len(nums) , nums , i)

            if len(nums) - nxt == i:

                return i

        return -1