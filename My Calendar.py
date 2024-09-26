class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for i, j in self.calendar:
            if i < end and start < j:
                return False
        self.calendar.append((start, end))
        return True