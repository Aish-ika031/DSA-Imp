class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=[]

        if len(strs)==0:

            res.append([""])

            return res

        if len(strs)==1:

            res.append([strs[0]])

            return res

        d1=defaultdict(list)

        for i in range(len(strs)):

            s=strs[i]

            d1["".join(sorted(s))].append(s)

        for i in d1:

            res.append(d1[i])
            
        return res