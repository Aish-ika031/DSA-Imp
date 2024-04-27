class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first_idx = -1

        last_idx = -1

        for i in range(len(nums)):

            if nums[i] == target:

                first_idx = i

                break
        
        for i in range(len(nums)):

            if nums[len(nums) - i - 1] == target:

                last_idx = len(nums) - i - 1

                break

            # if first_idx > 0 and last_idx > 0:

            #     break

        return [-1 , -1] if target not in nums else [first_idx , last_idx]
