class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums , res , curr):

            if len(curr) == len(nums):

                res.append(curr[:])

                return 

            for i in range(len(nums)):

                if nums[i] not in curr:

                    curr.append(nums[i])

                else:

                    continue

                backtrack(nums , res , curr)

                curr.pop()

        res = []

        backtrack(nums , res , [])

        return res
