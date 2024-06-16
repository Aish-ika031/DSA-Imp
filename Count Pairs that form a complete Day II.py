class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        d1 = defaultdict(int)

        cnt = 0

        for i in range(len(hours)):

            val = 24 - hours[i] % 24 

            cnt += d1[val % 24]

            d1[hours[i] % 24] += 1

        return cnt