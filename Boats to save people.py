class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        cnt , st , end = 0, 0 , len(people) - 1

        people.sort()

        while st <= end:

            cur = people[st] + people[end]

            if cur <= limit:

                cnt += 1

                st += 1

                end -= 1

            else:

                cnt += 1 

                end -= 1

        return cnt