class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        s = bin(num2)

        cnt = s.count('1')

        val  = 0

        for i in range(31, -1 , -1):

            if cnt == 0:

                break

            if num1 & (1<<i):

                val = val | (1<<i)

                cnt -= 1

        for i in range(32):

            if cnt ==0 :
                break

            if not(val & (1<<i)):

                val = val | (1<<i)

                cnt -= 1

        return val
