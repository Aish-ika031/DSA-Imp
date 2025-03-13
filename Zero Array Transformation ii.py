class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        cur_sum = 0

        cnt = 0

        diff = [0] * (len(nums) + 1)

        for i in range(len(nums)):

            while cur_sum + diff[i] < nums[i]:

                cnt += 1

                if cnt > len(queries):

                    return -1

                l , r , value = queries[cnt - 1]

                if r < i:

                    # cnt += 1

                    # cnt += 1

                    continue

                diff[max(l,i)] += value

                diff[r+1] -= value

                # cnt += 1

            cur_sum += diff[i]

        return cnt
