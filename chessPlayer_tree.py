from queue import*
class Tree:
    def __init__(self,x):
        self.store=[x,[]]

    def AddSuccessor(self,x):
        self.store[1]=self.store[1]+[x]
        return True

    def GetSuccessors(self):
        suc = self.store[1]
        return suc

    def CountSuccessors(self):
        suc = self.store[1]
        cnt = len(suc)
        return cnt

    def Get_LevelOrder(self):
        x=queue()
        x.enqueue(self.store)
        accum=[]
        while True:
            y=x.dequeue()
            if (y[0]==False):
                break
            else:
                v=y[1]
                accum=accum+[v[0]]
                for i in v[1]:
                    x.enqueue(i.store)
        return accum
