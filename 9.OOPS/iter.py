class lst():
    def __init__(self,l):
        self.list = l
        self.list_len = len(l)
        self.i1 = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i1 == self.list_len:
            raise StopIteration
        else:
            self.ele = self.list[self.i1]
            self.i1 += 1
            return self.ele



l = lst([1,2,3,4])
for ele in l:
    print(ele)