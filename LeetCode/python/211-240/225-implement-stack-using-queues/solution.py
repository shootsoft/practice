class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 =[]
        self.switch = 1
        self.length = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.switch == 1:
            self.q1.append(x)
            while(len(self.q2)>0):
                self.q1.append(self.q2.pop(0))
            self.switch = 2
        else:
            self.q2.append(x)
            while(len(self.q1)>0):
                self.q2.append(self.q1.pop(0))

            self.switch = 1

        self.length += 1

    # @return nothing
    def pop(self):

        if self.length ==0:
            return None

        self.length -= 1
        if self.switch == 1:
            return self.q2.pop(0)
        else:
            return self.q1.pop(0)


    # @return an integer
    def top(self):
        if self.length ==0:
            return None
        if self.switch == 1:
            return self.q2[0]
        else:
            return self.q1[0]

    # @return an boolean
    def empty(self):
        return self.length == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.top()
print s.pop()
print s.pop()
print s.pop()