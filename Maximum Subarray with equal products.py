class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        def cal_lcm(a,b):

            return (a*b) // math.gcd(a,b)

        ans = 1

        for i in range(len(nums)-1):

            for j in range(i+1, len(nums)):

                g = nums[i]

                l = 1

                res = 1


                for k in range(i , j+1):

                    g , l = gcd(nums[k],g) , cal_lcm(nums[k] , l)

                    res *= nums[k]

                if res == (l*g):

                    mx = j - i + 1

                    ans = max(ans , mx)

        return ans
