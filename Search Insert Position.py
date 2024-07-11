class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:

            return nums.index(target)

        st = 0

        while st < len(nums):

            if nums[st] < target:

                st += 1

            else:

                search_pos = st

                break

        return st