class Solution:
    def countSeniors(self, details: List[str]) -> int:

        cnt = 0
        
        for i in details :

            age = (list(i)[11:13])

            if int("".join(age)) > 60:

                cnt += 1

        return cnt