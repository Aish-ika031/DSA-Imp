class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        s = set(allowed)

        cnt = 0

        # var = 0

        for i in words:

            var = 0

            for cur_chr in i:

                if cur_chr in s:

                    # print(0)

                    var +=1 

                else:

                    var -=1 

            print(len(i) , var)

            if len(i) == var:

                # print(len(cur_chr) , var)

                cnt +=1 

        return cnt

                    