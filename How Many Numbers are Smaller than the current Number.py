class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        num = sorted(nums)

        mp = defaultdict(int)

        for i in range(len(num)):

            if num[i] not in mp:

                mp[num[i]] = i

        res = []

        for i in nums:

            res.append(mp[i])

        return res

