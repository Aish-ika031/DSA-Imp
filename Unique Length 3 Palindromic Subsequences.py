class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        cnt = 0

        # s1 =set()
        
        s2 =set(s)

        for i in s2:

            st = s.index(i)

            end = s.rindex(i)

            s1 = set()

            if st != end:

                s1 = s[st+1 : end]

                s1= set(s1)

            cnt += len(s1)

        return cnt

