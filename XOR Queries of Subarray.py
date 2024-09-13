class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l1=[]
        s1=0
        l2=[0]*len(arr)
        l2[0]=arr[0]
        s1=l2[0]
        for i in range(1,len(arr)):
            s1=s1^arr[i]
            l2[i]=s1
        ##print(l2)
        for i in queries:
            c=i[0]
            d=i[1]
            if c==0:
                l1.append(l2[d])
            else:
                l1.append(l2[c-1]^l2[d])
        return l1
            