class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0

        ten = 0

        # cnt = 0

        for i in range(len(bills)):

            if bills[i] == 5:

                # cnt += 1

                five += 1

            elif bills[i] == 10:

                if five > 0:

                    # curr_amt = curr_amt - 5

                    five -= 1

                    ten += 1

                else:

                    return False

            else:

                if five > 0 and ten > 0:

                    five -= 1

                    ten -= 1

                elif five >= 3:

                    five -= 3

                else:

                    return False

        return True 