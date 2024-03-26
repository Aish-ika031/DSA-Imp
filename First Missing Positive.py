class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        cur = set(nums)

        if max(nums) <= 0:

            return 1

        for i in range(1 , max(nums) + 1):

            if i not in cur:

                return i

        return max(nums) + 1