class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        s1 , st , curr_sum , mx = set() , 0 , 0 , 0

        for i in range(len(nums)):

            while st <i and (nums[i] in s1 or len(s1) >=k):

                curr_sum -= nums[st]

                s1.remove(nums[st])

                st += 1

            curr_sum += nums[i]

            s1.add(nums[i])

            if len(s1) == k:

                mx = max(mx , curr_sum)

        return mx
