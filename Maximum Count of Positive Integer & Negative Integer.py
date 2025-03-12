class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        pos_cnt , neg_cnt = 0 , 0

        for i in nums:

            if i > 0:

                pos_cnt += 1

            elif i< 0:

                neg_cnt += 1

        return max(pos_cnt , neg_cnt)
