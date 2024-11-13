class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def binary_search(arr , st , end , ele):

            while st <= end:

                mid = (st + end) // 2

                if nums[mid] < ele:

                    st = mid + 1

                else:

                    end = mid - 1

            return st

        nums.sort()

        cnt = 0

        for i in range(len(nums)):

            st , end = binary_search(nums , i + 1  , len(nums) - 1 , lower - nums[i]) , binary_search(nums , i + 1 , len(nums) - 1 , upper - nums[i] + 1)

            cnt += end - st

        return cnt


