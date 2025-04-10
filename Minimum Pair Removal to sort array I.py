class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        def check(nums):

            for i in range(1,len(nums)):

                if nums[i] == float("inf"):

                    return True

                if nums[i] < nums[i-1]:

                    return False

            return True

        def min_cnt(nums):

            idx = -1

            mn = float("inf")

            n = len(nums)

            for i in range(1, len(nums)):

                if nums[i] == float("inf"):

                    break

                if nums[i] + nums[i-1] < mn:

                    mn = min(mn , nums[i]+nums[i-1])

                    idx = i

            nums[idx-1] += nums[idx]

            for i in range(idx,n-1):

                nums[i] = nums[i+1]

            nums[n-1] = float("inf")

            return 


        cnt = 0

        while(not check(nums)):

            min_cnt(nums)

            cnt += 1

        return cnt

                
