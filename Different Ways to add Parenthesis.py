class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        if expression.isdigit():

            return [int(expression)]

        res = []

        s1 = ['-' ,'+','*']

        for k in range(len(expression)):

            if expression[k] in s1:

                l , r = self.diffWaysToCompute(expression[:k]) , self.diffWaysToCompute(expression[k+1:])

                for i in l:

                    for j in r:

                        if expression[k] == '+':

                            res.append(i + j)

                        elif expression[k] == '-':

                            res.append(i - j)

                        elif expression[k] =='*':

                            res.append(i * j)

        return res


        