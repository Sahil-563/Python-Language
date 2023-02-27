class sum_pair():
    def __init__(self,lst):
        self.list = lst
        self.list_len = len(lst)
        self.i1 = 0
        self.i2 =1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i2 == self.list_len:
            raise StopIteration
        else:
            self.sum = self.list[self.i1] + self.list[self.i2]
            self.i1 += 1
            self.i2 += 1
            return self.sum

l = sum_pair([1,2,3,4,5,6])
for ele in l:
    print(ele)