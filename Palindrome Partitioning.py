class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(s,path,res):

            if len(s)==0:

                res.append(path)

                return 

            for i in range(1,len(s)+1):

                s1=s[:i]

                if s1==s1[::-1]:

                    dfs(s[i:],path+[s1],res)

        res=[]

        dfs(s,[],res)
        
        return res