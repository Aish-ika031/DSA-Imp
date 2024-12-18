class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        res = prices
        
        st = []

        for i in range(len(prices)):

            while len(st) > 0 and prices[st[-1]] >= prices[i]:

                val = st.pop()

                res[val] -= prices[i]

            st.append(i)

        return res

