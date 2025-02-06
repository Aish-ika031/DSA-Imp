class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        mp = defaultdict(int)

        cnt = 0
        
        for i in range(len(nums)):

            for j in range(i+1 , len(nums)):

                val = 8*mp[nums[i] * nums[j]]

                cnt  += val

                mp[nums[i]*nums[j]] += 1

        return cnt
