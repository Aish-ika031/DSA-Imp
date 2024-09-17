class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1 , s2 = s1.split(" ") , s2.split(" ")

        res = []

        for i in s1:

            if i not in s2 and s1.count(i) == 1:

                res.append(i)

        for i in s2:

            if i not in s1 and s2.count(i) ==1 :

                res.append(i)

        return res