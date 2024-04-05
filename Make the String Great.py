class Solution:
    def makeGood(self, s: str) -> str:

        st=[]

        for i in range(len(s)):

            if len(st)>0 and abs(ord(st[-1])-ord(s[i]))==32:

                st.pop()

            else:

                st.append(s[i])

        # st.append(s[-1])

        return "".join(st)

        