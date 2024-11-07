class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        res = [0] * 32

        for i in candidates:

            cur = 0

            while i > 0:

                res[cur] += i & 1

                i = i >> 1

                cur += 1

        return max(res)
