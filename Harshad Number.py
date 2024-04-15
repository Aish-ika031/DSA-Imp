class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        def calculate_sum(num):

            sum_digit = 0

            while num > 0:

                sum_digit += num % 10

                num = num //10

            return sum_digit

        req = calculate_sum(x)

        return req if x % req == 0 else -1