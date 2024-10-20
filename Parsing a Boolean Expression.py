class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        s1 , s2 = [] , []

        for i in range(len(expression)):

            if expression[i] == '|' or expression[i] == '&' or expression[i] == '!':

                s1.append(expression[i])

            elif expression[i] == 'f' or expression[i] == 't' or expression[i] == '(' or expression[i] ==',':

                s2.append(expression[i])

            elif expression[i] == ')':

                cur = s1[-1]

                s1.pop()

                if cur == "&":

                    status = True

                    while s2[-1] != '(':

                        val = s2[-1]

                        if val == "f":

                            status = False

                        s2.pop()

                    s2.pop()

                    if status:

                        s2.append('t')

                    else:

                        s2.append('f')


                elif cur == '|':

                    status = False

                    while s2[-1] != '(':

                        val = s2[-1]

                        if val =='t':

                            status = True

                        s2.pop()

                    s2.pop()

                    if status:

                        s2.append('t')

                    else:

                        s2.append('f')

                elif cur == '!':

                    val = s2[-1]

                    s2.pop()

                    s2.pop()

                    if val == 't':

                        s2.append('f')

                    else:

                        s2.append('t')

        return False if s2[-1] == 'f' else True

                

