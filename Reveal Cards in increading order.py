from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        q1 = deque()

        res = [0] * len(deck)

        for i in range(len(deck)):

            q1.append(i)

        deck.sort()

        ptr = 0

        while len(q1) > 0:

            cur = q1.popleft()

            if len(q1) > 0:

                q1.append(q1.popleft())

            res[cur] = deck[ptr]

            ptr += 1

        return res
        