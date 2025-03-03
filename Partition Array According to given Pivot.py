class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        res=[]

        j=0

        for i in range(len(nums)):

            if nums[i]<pivot:

                res.append(nums[i])

        l1=[]

        for i in range(len(nums)):

            if nums[i]==pivot:

                l1.append(nums[i])
        l2=[]

        for i in range(len(nums)):

            if nums[i]>pivot:

                l2.append(nums[i])
                
        return res+l1+l2
