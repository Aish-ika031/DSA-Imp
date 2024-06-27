class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        avgs = []

        idx = 0

        n = len(nums)

        while idx < n:

            mn , mx = min(nums) , max(nums)

            nums.remove(mn)

            nums.remove(mx)

            # print(mn , mx)

            avg = (mn + mx) / 2

            # print(avgs)

            avgs.append(avg)

            idx += 2

        return min(avgs)