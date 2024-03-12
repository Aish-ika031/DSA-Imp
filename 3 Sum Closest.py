class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        m1=float("inf")

        nums.sort()

        for i in range(len(nums)):

            start,end=i+1,len(nums)-1

            while start<end:

                val=nums[i]+nums[start]+nums[end]

                if abs(val-target)<m1:

                    m1=abs(val-target)
                    diff=val

                elif (val-target)>0:
                    end=end-1

                else:
                    start=start+1
                    
        return diff