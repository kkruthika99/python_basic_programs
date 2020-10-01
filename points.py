class point:
def __init__(self,x=0,y=0):
self.x=x
self.y=y
def __add__(self, other):
c=point()
c.x=self.x+other.x
c.y=self.y+other.y
return c
def __str__(self):
return "x:"+str(self.x)+" y:"+str(self.y)
def input(self):
self.x = int(input("enter x co-ordinate"))
self.y = int(input("enter y coordinate"))
a= point()
b=point()
a.input()
b.input()
c=a+b
print(c)
