"""
Triangle Drawer

USAGE: python triangle.py n symbol

By: Darth Vader
Github: DarthVader1996
"""
import sys

"""
Triangle Class takes
a symbol and a number
and produces that
symbol n times
"""
class Triangle():

    def __init__(self, n, symbol):
        self.n = n
        self.symbol = symbol

    # Method 1
    def rightTriangle(self):
        for i in range(self.n):
            print(self.symbol*i)

    # Method 2
    def upsideTriangle(self):
        print(self.symbol*self.n)
        if(self.n > 0):
            self.n = self.n - 1
            self.upsideTriangle()

    # Method 3
    def slicedTriangle(self):
        print(" "*self.n, end="")
        print(self.symbol*(self.n//2))
        if(self.n > 0):
            self.n = self.n - 1
            self.slicedTriangle()

def main():
    n = sys.argv[1]
    symbol = sys.argv[2]
    drawing = Triangle(n, symbol)   

    # Demonstrate all three methods
    drawing.rightTriangle()
    drawing.slicedTriangle()
    drawing.upsideTriangle()

if __name__ == '__main__':
    main()



    
