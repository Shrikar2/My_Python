class rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
        
    def area(self):
        print("Area of the reactangle is",int(self.length)*int(self.width))

Area=rectangle(input("Enter the length of the rectangle:" ),input("Enter the width of the reactangle: "))
Area.area()
