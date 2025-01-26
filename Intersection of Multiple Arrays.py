class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        res = set(nums[0])

        for i in nums[1:]:

            res = res.intersection(set(i))

        return sorted(list(res))

