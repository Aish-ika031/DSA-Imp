class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1=0

        s2=0

        if len(nums)==0:

            return 0

        for i in range(1<<len(nums)):

            for j in range(len(nums)):
                
                if i&(1<<j)!=0:

                    s1=s1^nums[j]

            s2=s2+s1

            s1=0
            
        return s2