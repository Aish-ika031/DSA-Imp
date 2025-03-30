class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d1 = Counter()

        res = []

        st = 0

        end  =0

        for i in range(len(s)):

            d1[s[i]] = i

        for i in range(len(s)):

            end = max(end , d1[s[i]])

            if i == end:

                res.append(i - st +1)

                st = i + 1

        return res
