class CustomStack:

    def __init__(self, maxSize: int):

        self.st = []

        self.maxSize = maxSize

    def push(self, x: int) -> None:

        if len(self.st) < self.maxSize:

            self.st.append(x)
        

    def pop(self) -> int:

        if len(self.st) > 0:

            return self.st.pop()

        else:

            return -1
        

    def increment(self, k: int, val: int) -> None:

        mn = min(k , len(self.st))

        idx = 0

        while idx < mn:

            self.st[idx] += val

            idx += 1

        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)