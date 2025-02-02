class Solution:
    def check(self, nums: List[int]) -> bool:

        cnt = 0

        status = False
        
        for i in range(len(nums)):

            if nums[i] > nums[(i+1) % len(nums)]:

                cnt += 1

                if cnt > 1:

                    status = True

                    break

        return True if not status else False        
