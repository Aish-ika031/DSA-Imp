class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        a , b = [(i[0] , i[2]) for i in rectangles] , [(i[1] , i[3]) for i in rectangles]

        a.sort()

        b.sort()
        
        def check(intervals):

            cnt = 0 

            prev = -1

            for st , end in intervals:

                if prev <= st:

                    cnt += 1

                prev = max(prev, end)

            return cnt

        return True if max(check(a) , check(b)) >= 3 else False

