class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0

        for i in logs:

            if i=="./":

                continue

            elif i=="../":

                c=max(0,c-1)

            else:

                c=c+1
                
        return c