from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
       
        d1=Counter(students)

        for i in sandwiches:

            if not d1[i]:

                break

            d1[i]=d1[i]-1

        l1=[]

        for i in d1:

            l1.append(d1[i])

        return sum(l1)