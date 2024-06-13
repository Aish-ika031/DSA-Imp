class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()

        students.sort()

        cnt = 0

        for i in range(len(seats)):

            cnt += abs(seats[i] - students[i])

        return cnt