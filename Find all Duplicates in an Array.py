class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        mp = Counter(nums)

        res = []

        for i in mp:

            if mp[i] > 1:

                res.append(i)

        return res
        