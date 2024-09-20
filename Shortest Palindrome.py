class Solution:
    def shortestPalindrome(self, s: str) -> str:

        s1 = s[::-1]

        s2 = s + "0" + s1

        res = [0] * len(s2)

        j = 0

        for i in range(1 , len(s2)):

            while j > 0 and s2[i] != s2[j]:

                j = res[j - 1]

            if s2[i] == s2[j]:

                j += 1

                res[i] = j

        return s1[:len(s) - (res[-1])] + s
        