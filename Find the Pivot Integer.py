class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total_sum = (n*(n+1))//2

        half = sqrt(total_sum)

        return int(half) if int(half) * int(half) == total_sum else -1 