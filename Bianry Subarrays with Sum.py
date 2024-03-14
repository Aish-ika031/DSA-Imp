class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        curr_sum = 0

        mp = defaultdict(int)

        cnt = 0

        for i in range(len(nums)):

            curr_sum += nums[i]

            if curr_sum == goal:

                cnt += 1

            req = curr_sum - goal

            if req in mp and mp[req] > 0 :

                cnt += mp[req]

            mp[curr_sum] += 1

        return cnt