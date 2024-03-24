class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        mp = Counter(nums)

        for i in mp:

            if mp[i] > 1:

                return i