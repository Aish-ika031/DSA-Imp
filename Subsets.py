class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def recursion(nums , idx , res , curr):

            if idx >= len(nums):

                res.append(curr[::])

                return 
                
            curr.append(nums[idx])

            recursion(nums , idx+1 , res , curr)

            curr.pop()

            recursion(nums , idx+1 , res , curr)

        nums.sort()

        res = []

        recursion(nums , 0 , res , [])

        return res
        