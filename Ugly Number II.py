class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i=0
        j=0
        k=0
        res=[]
        res.append(1)
        s1=set()
        
        for v in range(1,n):
            a,b,c=res[i]*2,res[j]*3,res[k]*5
            if a==min(a,b,c):
                i=i+1
            if b ==min(a,b,c):
                j=j+1
            if c==min(a,b,c):
                k=k+1
            if min(a,b,c) not in s1:
                #s1.add(min(a,b,c))
                res.append(min(a,b,c))
        return res[-1]
            