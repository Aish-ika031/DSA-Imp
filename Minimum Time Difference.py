class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        m1=[]
        
        for i in timePoints:
            m=int(i[i.index(':')+1:])
            hrs=int(i[:i.index(':')])
            # if hrs>12:
            #     hrs=hrs-12
            m1.append(hrs*60+m)
    
        
        m1.sort()
        
        print(m1)
        
        min_time=float("inf")
        
        for i in range(len(m1)-1):
            
            min_time=min(min_time,m1[i+1]-m1[i])
        
        print(min_time)
        
        # print(m1[0]+24*60-m1[len(m1)-1])
            
        return min(min_time,m1[0]+24*60-m1[len(m1)-1])
        
        # return min_time