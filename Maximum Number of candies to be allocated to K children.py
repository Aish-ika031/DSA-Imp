class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if sum(candies) < k:

            return 0
        
        def func(candies , k , size):

            if size == 0:

                return 1

            cnt  = 0

            for i in candies:

                cnt += i // size

                if cnt >=k:

                    return 1

            return 0

        st , end = 1 , max(candies)

        while st < end:

            mid  = st + (end -st)//2

            if func(candies , k , mid) == 1:

                st = mid + 1

            else:

                end = mid

        return st if func(candies , k , st) == 1  else st - 1

            

