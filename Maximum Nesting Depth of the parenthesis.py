class Solution:
    def maxDepth(self, s: str) -> int:

        st = []

        mx = 0

        for i in s:

            if i == '(':

                st.append(i)

            elif i == ')':

                st.pop()

            mx = max(mx , len(st))

        return mx
        