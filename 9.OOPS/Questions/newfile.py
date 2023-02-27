class lst():
    def __init__(self,l):
        self.l=l
    def loops(self):
        for ele in self.l:
            print(ele)
    
    def __iter__(self):
        return self
    def nex_val(self):
        pass


x=lst([12,3,4,5,6])
x.loops()


