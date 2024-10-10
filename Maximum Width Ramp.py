class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        st = []

        for i in range(len(nums)):

            if not st or nums[i] < nums[st[-1]]:

                st.append(i)

        mx = 0

        for j in range(len(nums)-1 , -1 , -1):

            while len(st) > 0 and nums[j] >= nums[st[-1]]:

                mx = max(mx , j - st.pop())

        return mx