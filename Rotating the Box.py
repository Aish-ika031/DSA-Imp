class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        c , r = len(box) , len(box[0])

        res = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):

            for j in range(c):

                res[i][j] = box[j][i]

        for i in range(r):

            for j in range(c//2):

                res[i][j], res[i][c - 1 - j] = res[i][c-1-j], res[i][j]

        for i in range(len(res[0])):

            cnt = len(res) - 1

            for j in range(len(res)-1 , -1 , -1):

                # cnt = r - 1

                if res[j][i]=='#':

                    res[j][i] ='.'

                    # cnt -= 1

                    res[cnt][i] = '#'

                    cnt -= 1

                elif res[j][i] == '*':

                    cnt = j - 1

        return res


