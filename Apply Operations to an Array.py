class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):

            if nums[i] == nums[i+1]:

                nums[i] = nums[i] * 2 

                nums[i+1] = 0

        print(nums)

        res = [0] * len(nums)

        idx = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                res[idx] = nums[i]

                idx += 1

            # print(res)

        return res
