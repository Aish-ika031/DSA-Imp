class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def recur(nums, target , st, cur):

            if st == len(nums):

                if cur == target:

                    return 1

                else:

                    return 0

            s1 , s2 = recur(nums, target , st + 1, cur + nums[st]) , recur(nums, target , st + 1 , cur - nums[st])

            return s1 + s2

        return recur(nums, target , 0 , 0)
