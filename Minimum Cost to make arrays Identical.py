class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        
        cur = 0

        for i in range(len(arr)):

            cur += abs(arr[i] - brr[i])

        a , b = sorted(arr) , sorted(brr)

        cur2 =0

        for i in range(len(a)):

            cur2 += abs(a[i] - b[i])

        return min(cur , cur2 + k)

        
