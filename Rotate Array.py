class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums , i , j):

            while i < j:

                nums[i] , nums[j] = nums[j] , nums[i]

                i=i+1

                j=j-1

        k = k%len(nums)

        reverse(nums, 0 , len(nums) - k - 1)

        print(nums)

        reverse(nums , len(nums) - k , len(nums)-1)

        print(nums)

        reverse(nums , 0 , len(nums)-1)