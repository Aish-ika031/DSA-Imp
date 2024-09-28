class MyCalendarTwo:

    def __init__(self):
        
        self.d1 = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        
        self.d1[start] += 1

        self.d1[end] -= 1

        cnt = 0

        for i in sorted(self.d1.keys()):

            cnt += self.d1[i]

            if cnt > 2:

                self.d1[start] -= 1

                self.d1[end] += 1

                return False

        return True




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)