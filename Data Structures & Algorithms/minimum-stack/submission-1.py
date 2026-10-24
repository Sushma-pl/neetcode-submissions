class MinStack:

    def __init__(self):
        self.st = []
        self.minele = float('inf')


    def push(self, val: int) -> None:
        if not self.st :
            self.st.append(val)
            self.minele = val
        elif self.minele <= val:
            self.st.append(val)
        elif self.minele > val:
            self.st.append(2*val-self.minele)
            self.minele = val
        # print(self.st, self.minele)
            

    def pop(self) -> None:
        
        if self.st[-1] < self.minele:
            self.minele =  2*self.minele - self.st[-1]
        
        self.st.pop()
        # print(self.st, self.minele)

    def top(self) -> int:
        if self.st[-1] < self.minele:
            return self.minele
        else:
            return self.st[-1]
        
        # self.st.pop()
        # print(self.st, self.minele)
        
        

    def getMin(self) -> int:
        # print(self.st, self.minele)
        return self.minele
