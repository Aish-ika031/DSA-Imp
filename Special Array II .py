class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        pref = [0] * len(nums)

        pref[0] = 0
        
        for i in range(1 , len(nums)):

            pref[i]= pref[i-1] + 1 if nums[i] % 2 == nums[i-1] % 2 else pref[i-1]

        j = 0

        res = [False] * len(queries)

        for i in queries:

            res[j] = True if pref[i[1]] - pref[i[0]] == 0 else False

            j += 1

        return res
