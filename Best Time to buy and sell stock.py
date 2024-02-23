class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # nums = sorted(prices)

        # if prices == prices.sort(reverse = True):

        #     return 0

        mx_profit = 0

        curr_min = float("inf")

        for i in range(len(prices)):

            curr_min = min(curr_min , prices[i])

            mx_profit = max(mx_profit , prices[i] - curr_min)

            print(mx_profit)

        return mx_profit

