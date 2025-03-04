class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        status = False

        while n > 0:

            if n % 3 == 2:

                status = True

                break

            n = n // 3

        return True if not status else False
