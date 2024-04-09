from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        q1 = deque()

        for i in range(len(tickets)):

            q1.append(i)

        t = 0

        while q1:

            t += 1

            cur = q1.popleft()

            tickets[cur] -= 1

            if k == cur and tickets[cur] == 0:

                return t

            if tickets[cur] != 0:

                q1.append(cur)

        return cur


        
