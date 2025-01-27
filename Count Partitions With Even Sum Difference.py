class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        cnt = 0
        
        for i in range(len(nums)):

            a1 , a2 = nums[0:i+1] , nums[i+1:]

            # print(a1,a2)

            if len(a1) > 0 and len(a2) > 0:

                if abs(sum(a1) - sum(a2)) % 2 == 0:

                    # print(a1,a2)

                    cnt += 1

        return cnt
