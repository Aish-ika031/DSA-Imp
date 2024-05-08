class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:

            return False

        v ,c = 0, 0

        for i in word:

            if i.isalpha():

                if i in ['A', 'E' , 'I', 'O','U' , 'a' ,'e' ,'i', 'o','u']:

                    v += 1

                else:

                    c += 1

            elif not i.isdigit():

                # print(i)

                return False

        if v >= 1 and c >= 1:

            return True

        else:

            return False
        