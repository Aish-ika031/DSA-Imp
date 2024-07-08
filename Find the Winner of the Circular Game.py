from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        q1 = deque([i for i in range(1 , n+1)])

        while len(q1) > 1:

            for i in range(1 , k):

                q1.append(q1.popleft())

                # q1.pop()

            q1.popleft()


        return q1.popleft()