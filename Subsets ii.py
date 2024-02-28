class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def recursion(nums , idx , res , curr):

            if idx >= len(nums):

                res.append(curr[::])
                
                return

            val = nums[idx]

            curr.append(val)

            recursion(nums , idx+1 , res , curr)

            curr.pop()

            while idx + 1 < len(nums) and nums[idx+1] == nums[idx]:

                idx += 1

            recursion(nums , idx+1 , res , curr)
            

        res = []

        # curr = []

        nums.sort()

        recursion(nums , 0 , res , [])

        return res
        