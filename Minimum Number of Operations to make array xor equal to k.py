class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        xor = nums[0]

        for i in nums[1:]:

            xor = xor ^ i

        cnt = 0 

        while k > 0 or xor > 0:

            if k % 2 != xor % 2:

                cnt += 1

            k = k // 2

            xor = xor // 2

        return cnt