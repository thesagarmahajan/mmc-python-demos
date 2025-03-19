class Calculations:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2
    
    def sub(self):
        return self.n1 - self.n2
    
    def mult(self):
        return self.n1 * self.n2
    
    def divi(self):
        return self.n1 / self.n2
    
if __name__=="__main__":
    c = Calculations(6,2)
    print(c.add())
