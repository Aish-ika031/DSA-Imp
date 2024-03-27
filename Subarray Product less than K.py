class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k==0 or k==1:

            return 0

        left=0

        c=0

        val=1

        for i in range(0,len(nums)):

            val=val*nums[i]

            while val>=k:

                val=val/nums[left]

                left=left+1

            c=c+(i-left+1)
            
        return c