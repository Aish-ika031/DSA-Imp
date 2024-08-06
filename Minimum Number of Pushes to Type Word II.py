class Solution:
    def minimumPushes(self, word: str) -> int:
        
        res = [0] * 26

        for c in word:

            res[ord(c) - ord("a")] += 1

        res.sort(reverse=True)

        total_pushes = 0

        for i in range(26):

            if res[i] == 0:

                break

            total_pushes += (i // 8 + 1) * res[i]

        return total_pushes