__author__ = 'yinjun'

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.length = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        
        self.length +=1 
        self.s1.append(x)
        
                

    # @return nothing
    def pop(self):

        if self.length ==0:
            return None

        self.length -= 1

        if len(self.s2)>0:
            return self.s2.pop()

        if len(self.s1) ==0:
            return None

        while len(self.s1) >0:
            self.s2.append(self.s1.pop())

        return self.s2.pop()


    # @return an integer
    def peek(self):
        
        if len(self.s2)>0:
            return self.s2[len(self.s2)-1]

        if len(self.s1) ==0:
            return None

        while len(self.s1) >0:
            self.s2.append(self.s1.pop())

        return self.s2[len(self.s2)-1]

    
    # @return an boolean
    def empty(self):
        return self.length ==0 