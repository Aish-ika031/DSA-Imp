class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in nums:
            
            curr = str(i)
            
            curr = list(map(int , curr))
            
            print(curr)
            
            curr_mx = max(curr)
            
            curr_length = len(curr)
            
            curr_num = int(str(curr_mx)*curr_length)
            
            print(curr_num)
            
            res += curr_num
            
            print(res)
            
        return res
        