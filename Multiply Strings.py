class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':

            return '0'

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1 , - 1, -1):

            for j in range(len(num2) - 1 , -1 , -1):

                val = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                a , b = i + j , i + j + 1

                carry = val + res[b]

                res[b] = carry % 10

                res[a] += carry // 10

        return "".join(map(str, res)).lstrip('0')
        
