class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        min_len = float("inf")

        status = False

        for i in range(len(nums)):

            cur = nums[i]

            for j in range(i , len(nums)):

                cur = cur | nums[j]

                if cur >= k:

                    status = True

                    min_len = min(min_len , j - i + 1)

        return min_len if status else -1
