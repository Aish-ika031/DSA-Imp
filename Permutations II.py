class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums , res , curr , cnt):

            if len(curr) == len(nums):

                res.append(curr[:])

                return 

            for i in cnt:

                if cnt[i]>0:

                    curr.append(i)

                    cnt[i] -= 1

                    backtrack(nums , res , curr , cnt)

                    curr.pop()

                    cnt[i] += 1

        res = []

        cnt = Counter(nums)

        backtrack(nums , res , [] , cnt)

        return res
