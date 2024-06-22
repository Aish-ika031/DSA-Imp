class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        cnt = 0

        for i in range(len(nums)):

            if nums[i] % 3:

                cnt += 1

        return cnt