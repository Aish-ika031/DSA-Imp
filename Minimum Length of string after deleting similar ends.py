class Solution:
    def minimumLength(self, s: str) -> int:

        st = 0 

        end = len(s) - 1

        while st < end and s[st] == s[end]:

            curr = s[st]

            while st <= end and s[st] == curr:

                st += 1

            while end > st and s[end] == curr:

                end -= 1

        return end - st + 1 
        