class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        d1 , d2 = {s[i] : i for i in range(len(s))} , {t[i] : i for i in range(len(t))}

        print(d1 , d2)

        ans = 0

        for i in s:

            ans += abs(d1[i] - d2[i])

        return ans