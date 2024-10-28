class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        mx_len = 0

        visited_nums = set(nums)

        for i in nums:

            curr_len = 0

            curr = i

            while curr in visited_nums:

                curr_len += 1

                if curr * curr > 10**5:

                    break

                curr *= curr

            mx_len = max(mx_len , curr_len)

        if mx_len >= 2:

            return mx_len

        else:

            return -1
