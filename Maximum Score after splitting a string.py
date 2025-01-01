class Solution:
    def maxScore(self, s: str) -> int:
        
        mx = 0

        for i in range(len(s)):

            s1 , s2 = s[:i+1] , s[i+1:]

            if len(s1) !=0 and len(s2) !=0:

                mx = max(mx , (s1.count('0') + s2.count('1')))

        return mx
