class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        left_prod = 1

        mx = float("-inf")

        for i in range(0 , len(nums)):

            left_prod = left_prod * nums[i]

            print(left_prod)

            mx = max(mx , left_prod)

            if left_prod == 0:

                left_prod = 1

            print(mx)

        right_prod = 1

        for i in range(len(nums) - 1 , -1 , -1):

            right_prod = right_prod * nums[i]

            mx = max(mx , right_prod)

            if right_prod == 0:

                right_prod = 1

        return mx
        