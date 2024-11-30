class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        cnt = [0] * len(nums)

        for i in queries:

            cnt[i[0]] += 1

            cur_val = i[1]

            if cur_val < len(nums) - 1:

                cnt[i[1] + 1] -= 1

        res = 0

        for i in range(len(nums)):

            res += cnt[i]

            if res < nums[i]:

                return False

        return True
