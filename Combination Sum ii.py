class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates,target,unique,result,i):
            if target==0:
                #print(unique)
                unique=list(unique)
                result.append(unique)
            status=0
            while i<len(candidates) and target>=candidates[i]:
                if status!=candidates[i]:
                    unique.append(candidates[i])
                    backtrack(candidates,target-candidates[i],unique,result,i+1)
                    unique.pop()
                    status=candidates[i]
                i=i+1
        result=[]
        candidates.sort()
        backtrack(candidates,target,[],result,0)
        return result
            