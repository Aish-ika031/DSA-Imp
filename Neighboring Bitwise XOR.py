class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        val = 0

        for i in range(len(derived)):

            val = val ^ derived[i]

        return True if val == 0 else False
