class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        mp = Counter(arr)

        for i in arr:

            if i == 0:

                if mp[i] > 1:

                    return True


            else:
                
                if i*2 in mp:

                    return True

            # if i == 0:

            #     if mp[i] > 1:

            #         return True


        return False


