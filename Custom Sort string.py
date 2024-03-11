class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        cnt = Counter(s)

        res = ""

        for i in order:

            if i in cnt:

                res = res + (cnt[i] * i)

                cnt[i] = 0

            print(res)

        for i in cnt:

            if cnt[i] > 0:

                res = res + i*cnt[i]

        return res