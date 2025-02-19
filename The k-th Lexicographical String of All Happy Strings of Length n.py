class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        cnt = 0

        for i in range(3**n):

            s = ""

            for x in range(n):

                s = "abc"[i//3**x%3]+s

            flag = True

            for i in range(1, len(s)):

                if s[i] == s[i-1]: flag = False

            if flag:

                cnt += 1

                if cnt == k:

                    return s
                    
        return ""
