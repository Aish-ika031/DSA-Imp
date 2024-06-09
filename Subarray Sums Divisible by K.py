class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        res = [0] * k

        res[0] = 1

        cur = 0

        cnt = 0

        for i in range(len(nums)):

            cur = (cur + nums[i] % k + k) % k

            cnt += res[cur]

            res[cur] += 1

        return cnt