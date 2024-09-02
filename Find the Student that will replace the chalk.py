class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        if k % sum(chalk) == 0:

            return 0

        rem = k % sum(chalk)

        idx = 0

        for i in range(len(chalk)):

            rem -= chalk[i]

            if rem < 0 :

                return i 