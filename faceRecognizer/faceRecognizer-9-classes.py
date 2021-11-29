class Rectangle:
    def __init__(self,c,w,l):    #method
        self.width=w
        self.length=l
        self.color=c
    def area(self):
        self.area=self.width*self.length
        return self.area
    def per(self):
        self.perimeter=2*self.width+2*self.length
        return self.perimeter
c1='red'
w1=3
l1=4
rect1=Rectangle(c1,w1,l1)   #object of rectangle
#print('Rectangle 1 is',rect1.color,'with area',rect1.area)
areaRect1=rect1.area()
print(areaRect1)
per1=rect1.per()
print('Rectangle 1 has perimeter:',per1)


c2='blue'
w2=3
l2=8
rect2=Rectangle(c2,w2,l2)   #object of rectangle
#print('Rectangle 1 is',rect1.color,'with area',rect1.area)
areaRect2=rect2.area()
print(areaRect2)
print('Rectangle 1 is:',rect1.color)
