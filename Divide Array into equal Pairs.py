class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        cnt = Counter(nums)

        for i in cnt:

            if cnt[i] % 2:

                return False

        return True
