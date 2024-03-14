class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height)==0:

            return 0

        l_max=[0]*len(height)

        r_max=[0]*len(height)

        max_water=0

        l_max[0],r_max[len(height)-1]=height[0],height[len(height)-1]

        for i in range(1,len(height)):

            if height[i]>l_max[i-1]:

                l_max[i]=height[i]

            else:

                l_max[i]=l_max[i-1]

        for i in range(len(height)-2,-1,-1):

            if height[i]>r_max[i+1]:

                r_max[i]=height[i]

            else:

                r_max[i]=r_max[i+1]

        #print(l_max)
        #print(r_max)

        for i in range(len(height)):

            val=min(l_max[i],r_max[i])

            max_water=max_water+(val-height[i])

        return max_water