class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        ans = 0

        mx = 1

        for i in range(1 , len(colors) + k - 1):

            if colors[i%len(colors)] != colors[(i+len(colors)-1)%len(colors)]:

                mx += 1

            else:

                mx = 1

            if mx >= k:

                ans += 1

        return ans

