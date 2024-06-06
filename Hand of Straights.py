class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:

            return False

        cnt = Counter(hand)

        val = sorted(cnt.keys())

        for i in val:

            if cnt[i]:

                cur = cnt[i]

                for j in range(i , i + groupSize):

                    if cnt[j] < cur:

                        return False

                    cnt[j] -= cur

        return True