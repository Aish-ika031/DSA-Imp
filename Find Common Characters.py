class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        mn = [float('inf')] * 26

        for i in words:

            cur = [0 for i in range(26)]

            for j in i:

                cur[ord(j) - ord('a')] += 1

            for k in range(26):

                mn[k] = min(mn[k], cur[k])

        res = []

        for i in range(26):

            res = res + [chr(i + ord('a'))] * mn[i]

        return res