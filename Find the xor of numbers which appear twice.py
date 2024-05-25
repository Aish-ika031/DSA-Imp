class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        mp = Counter(nums)

        xor = 0

        for i in mp:

            if mp[i] == 2:

                xor = xor ^ i

        return xor