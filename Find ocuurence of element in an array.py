class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        res = []

        idx = []

        for i in range(len(nums)):

            if nums[i] == x:

                idx.append(i)

        for q in queries:

            res.append(idx[q - 1]) if q - 1 < len(idx) else res.append(-1)

        return res