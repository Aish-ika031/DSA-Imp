class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        st = []

        s1 = list(s)

        for i in range(len(s)):

            if s[i] == '(':

                st.append(i)

            elif s[i] ==')':

                if len(st) > 0:

                    st.pop()

                else:

                    s1[i] = "" 

        if len(st) > 0:

            for i in range(len(st)):

                s1[st[i]] = ""

        return "".join(s1)

