class Solution:
    def clearDigits(self, s: str) -> str:
        
        s = list(s)

        idx = 0

        for i in range(len(s)):

            if s[i].isdigit():

                idx -= 1

            else:

                s[idx] = s[i]

                idx += 1

        return "".join(s[:idx])