class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l1=[]
        for i in range(len(nums)):
            val=int(nums[i],2)
            l1.append(val)
        l1=set(l1)
        a=len(nums[0])
        b=int(pow(2,a))
        for i in range(b):
            if i not in l1:
                s1=bin(i)[2:]
                return "0"*(a-len(s1))+s1
        return "-1"
