class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mod = 0

        d1 = {0 : -1}

        for i in range(len(nums)):

            mod = (mod + nums[i]) % k

            if mod in d1:

                if i - d1[mod] > 1:

                    return True

            else:

                d1[mod] = i

        return False