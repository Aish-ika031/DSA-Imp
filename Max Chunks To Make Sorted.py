class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        a = sorted(arr)

        cnt = 0

        s1 , s2 = 0 , 0

        for i in range(len(arr)):

            s1 , s2 = s1 + arr[i] , s2 + a[i]

            cnt = cnt + 1 if s1 == s2 else cnt + 0

        return cnt
