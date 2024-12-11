class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        j , mx = 0 , 0

        for i in range(len(nums)):

            while nums[i] - nums[j] > 2 * k:

                j += 1

            mx = max(mx , i - j + 1)

        return mx
