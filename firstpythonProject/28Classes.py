class Point:
    #Conctructor
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move!")
    def draw(self):
        print("Draw..")


p1 = Point(1,2)
print(p1.x, p1.y)
p1.draw()

p2 = Point(3,4)
print(p2.x, p2.y)
p2.draw()