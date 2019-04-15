class queue:
    def __init__(self):
        self.store=[]
        self.cnt = 0

    def enqueue(self,value):
        self.store=self.store+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def dequeue(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.store[0]
            self.cnt=self.cnt-1
            self.store=self.store[1:]
            return [True,r]
