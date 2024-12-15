class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        res = []

        ans = 0

        for i in classes:

            cur_ratio = (i[0]-i[1])/(i[1]*(i[1]+1))

            heapq.heappush(res , [cur_ratio , i[0],i[1]])

        while extraStudents > 0:

            val = heapq.heappop(res)

            x , y = val[1] + 1 , val[2] + 1

            cur_ratio = (x-y)/(y*(y+1))

            heapq.heappush(res , [cur_ratio , x , y])

            extraStudents -= 1

        cnt = 0

        while len(res) > 0:

            val = heapq.heappop(res)

            cnt += val[1]/val[2]

        ans = cnt/len(classes)

        return ans

