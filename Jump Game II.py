class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jump=0

        end=0

        maxi=0

        for i in range(len(nums)-1):

            val=i+nums[i]

            maxi=max(maxi,val)

            if i==end:

                min_jump=min_jump+1

                end=maxi

        return min_jump