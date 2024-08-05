class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        cnt = Counter(arr)

        a = 0

        for i in cnt:

            if cnt[i] == 1:

                a += 1

            if a == k:

                return i

        if a != k:

            return ""
