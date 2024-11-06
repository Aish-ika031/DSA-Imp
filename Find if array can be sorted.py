class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def check(a , b):

            return bin(a).count('1') == bin(b).count('1')

        for k in range(len(nums)):

            for i in range(len(nums) - 1):

                status = check(nums[i] , nums[i+1])

                if status and nums[i] > nums[i+1]:

                    nums[i] , nums[i+1] = nums[i+1] , nums[i]

        return True if nums == sorted(nums) else False
