class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        b1 , b2 = 0 , 0

        m1 , m2 = 0 , 0

        res = [0]*len(boxes)

        for i in range(len(boxes)):

            res[i] += m1

            b1 += int(boxes[i])

            m1 += b1

        for i in range(len(boxes) - 1 , -1 , -1):

            res[i] += m2

            b2 += int(boxes[i])

            m2 += b2

        return res
