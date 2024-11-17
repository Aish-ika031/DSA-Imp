class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        

        st , end = [0] * len(nums) , [0] * len(nums)

        for i in range(len(nums) - 1):

            st[i + 1] = st[i] + nums[i]

            end[len(nums) - i - 2] = end[len(nums) - i - 1] + nums[len(nums) - 1 - i]

        cnt = 0

        for i in range(len(nums)):

            if nums[i] == 0:

                if st[i] == end[i]:

                    cnt += 2

                elif abs(st[i] - end[i]) == 1:

                    cnt += 1

        return cnt

