class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def func(r , b):

            flag , i = True , 1

            while True:

                if flag:

                    if r < i:

                        return i - 1

                    r -= i

                else:

                    if b < i:

                        return i - 1

                    b -= i

                i += 1

                flag = not flag

        return max(func(red , blue) , func(blue , red))