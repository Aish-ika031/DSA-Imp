class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def sieve(n):

            res = []

            res.append(0)

            prime = [True for i in range(n+1)]
            p = 2
            while (p * p <= n):

                if (prime[p] == True):

                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1

            for p in range(2, n+1):
                if prime[p]:

                    res.append(p)

            return res

        res = sieve(1000)

        print(res)

        prev = 0

        for i in range(len(nums)):

            diff = nums[i] - prev

            cur = 0

            while len(res) > cur + 1 and diff > res[cur + 1]:

                cur += 1

            nums[i] = nums[i] - res[cur]

            if nums[i] <= prev:

                return False

            prev = nums[i]

        for i in range(1 , len(nums)):

            if nums[i] <= nums[i - 1]:

                return False

        return True
