class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort()

        res = []

        res.append(folder[0])

        for i in range(1 , len(folder)):

            prev = res[-1]

            prev += "/"

            if folder[i].startswith(prev) == False:

                res.append(folder[i])

        return res
