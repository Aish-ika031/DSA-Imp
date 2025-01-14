class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        res = [0] * len(A)

        mp = defaultdict(int)

        common_cnt =0

        for i in range(len(A)):

            mp[A[i]] += 1

            if mp[A[i]] == 2:

                common_cnt += 1

            mp[B[i]] += 1

            if mp[B[i]] == 2:

                common_cnt += 1

            res[i] = common_cnt


        return res
