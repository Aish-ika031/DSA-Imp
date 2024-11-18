class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l1=[0 for _ in range(len(code))]
        if k>0:
            for i in range(len(code)):
                if (i+k)>=len(code):
                    l2=code[:abs((len(code)-(i+k)))+1]
                    s1=sum(code[i+1:])
                    l1[i]=sum(l2)+s1
                else:
                    l1[i]=sum(code[(i+1)%len(code):(i+k)%len(code)+1])
            return l1
        elif k<0:
                code=code[::-1]
                k=abs(k)
                for i in range(len(code)):
                    if (i+k)>=len(code):
                        l2=code[:abs((len(code)-(i+k)))+1]
                        s1=sum(code[i+1:])
                        l1[i]=sum(l2)+s1
                        ##print(l2)
                        ##print(s1)
                    else:
                        l1[i]=sum(code[(i+1)%len(code):(i+k)%len(code)+1])
                return l1[::-1]
        else:
            return l1
