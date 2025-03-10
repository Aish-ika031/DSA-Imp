class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        s1 =set()

        cnt =0

        for i in range(len(fruits)):

            for j in range(len(fruits)):

                if baskets[j] >= fruits[i] and j not in s1:

                    s1.add(j)

                    cnt += 1

                    break

        val = len(fruits) - cnt

        return val
