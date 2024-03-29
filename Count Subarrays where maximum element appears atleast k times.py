class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        st , cnt , res = 0 , 0 , 0

        mx = max(nums)

        for i in nums:

            if i == mx:

                cnt += 1

            while cnt >= k:

                if nums[st] == mx:

                    cnt -= 1

                st += 1

            res += st

        return res


        