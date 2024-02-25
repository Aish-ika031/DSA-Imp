class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        cnt = Counter(nums)
        
        print(cnt)
        
        for i in cnt:
            
            if cnt[i] != 1 and cnt[i] != 2:
                
                return False
            
        return True