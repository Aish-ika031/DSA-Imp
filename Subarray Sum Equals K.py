class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d1 = defaultdict(int)

        curr_sum = 0

        cnt = 0

        for i in nums:

            curr_sum += i

            if curr_sum - k in d1:

                cnt += d1[curr_sum-k]

            if curr_sum == k:

                cnt += 1

            d1[curr_sum] += 1

        return cnt