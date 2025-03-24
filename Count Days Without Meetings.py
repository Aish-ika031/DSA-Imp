class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        cur_end = 0

        # print(meetings)

        cnt = 0

        for i in meetings:

            st ,end = i[0] , i[1]

            if st > cur_end + 1:

                cnt += st - cur_end  -1

            cur_end = max(cur_end , end)

        return cnt + days - cur_end

