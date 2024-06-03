class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        st , end = 0 , 0

        while st < len(s) and end < len(t):

            if s[st] == t[end]:

                end += 1

            st += 1

        return len(t) - end