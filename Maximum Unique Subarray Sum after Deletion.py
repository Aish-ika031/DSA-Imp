class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            
            return nums[0]
        
        s1 = set()
        
        mx_sum = 0
        
        for i in range(len(nums)):
            
            if nums[i] > 0 and nums[i] not in s1:
                
                mx_sum += nums[i]
                
                s1.add(nums[i])
                
        if mx_sum == 0:
            
            mx_sum+= max(nums)
        
        return mx_sum
            
