class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        while k != 0:

            mn = min(nums)

            val = mn * multiplier

            idx = nums.index(mn)

            nums[idx] = val

            k -= 1

        return nums

