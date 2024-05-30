class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        if len(arr) == 1:

            return 0

        res = 0

        for i in range(len(arr)):

            xor = 0 
            
            for j in range(i , len(arr)):

                xor = xor ^ arr[j]

                if xor == 0:

                    res += j - i 

        return res

