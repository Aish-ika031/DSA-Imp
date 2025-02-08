from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        
        self.container=defaultdict(SortedList)
        self.d1={}
        

    def change(self, index: int, number: int) -> None:
        if index  in self.d1:
            self.container[self.d1[index]].remove(index)
        
        self.container[number].add(index)
        self.d1[index]=number

    def find(self, number: int) -> int:
#         idx=float("inf")
        
#         status=False
        
#         if number not in self.container:
#             status=True
        
#         for i in self.container:
#             print(0)
            
#             if self.container[i]==number:
#                 idx=min(idx,i)
            
#             print(idx)
                
#         return idx if status==False else -1
        
        if len(self.container[number])>0:
            return self.container[number][0]
        
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
