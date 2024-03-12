class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d1 = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        
        res=[""]

        for i in digits:

            curr=[]

            for j in res:

                for k in d1[i]:

                    curr.append(j+k)
            
            res=curr
            
        if len(res)==1:
            
            return []
        
        return res