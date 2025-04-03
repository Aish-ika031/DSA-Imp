class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        mx_left=0

        mx_right=nums[-1]

        left,right=[0]*len(nums),[0]*len(nums)

        for i in range(0,len(nums)-1):

            left[i]=mx_left

            mx_left=max(mx_left,nums[i])

        for i in range(len(nums)-1,-1,-1):

            right[i]=mx_right

            mx_right=max(mx_right,nums[i])

        ans=0

        for i in range(1,len(nums)-1):

            ans=max(ans,(left[i]-nums[i])*right[i])

        return ans
