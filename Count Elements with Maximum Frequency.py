class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)

        mx = max(cnt.values())

        res = 0

        for i in cnt:

            if cnt[i] == mx:

                res += cnt[i]

        return res