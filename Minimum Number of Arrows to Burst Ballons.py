class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        prev = points[0][1]

        cnt = 1

        for i in points[1:]:

            if i[0] > prev:

                cnt += 1

                prev = i[1]

            prev = min(prev , i[1])

        return cnt