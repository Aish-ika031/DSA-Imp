class ProductOfNumbers:

    def __init__(self):

        self.l1 = []

        self.prod = 1
        

    def add(self, num: int) -> None:

        if num != 0 :

            self.prod *= num

            self.l1.append(self.prod)

        else:

            self.l1 =[]

            self.prod = 1

        
        

    def getProduct(self, k: int) -> int:

        if len(self.l1) < k:

            return 0

        elif len(self.l1) == k:

            return self.l1[-1]

        else:

            val = self.l1[-1] // self.l1[-k - 1]

        return val

        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
