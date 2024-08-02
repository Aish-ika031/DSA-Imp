class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        single_sum , double_sum = 0 , 0

        for i in nums:

            if len(str(i)) == 1:

                single_sum += i

            else:

                double_sum += i

        return True if single_sum != double_sum else False