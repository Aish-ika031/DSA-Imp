class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        mx = 0

        for i in nums:

            curr = i

            if curr - 1 not in nums:

                val = curr

                cnt = 1

                while val + 1 in nums:

                    cnt += 1

                    val += 1

                mx = max(mx , cnt)

        return mx

                

        