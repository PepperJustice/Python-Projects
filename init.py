
# create a class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        def myfunc(self):
            print("Hi my name is " + self.name)

p1= Person("Slim Shady", 52)
p1.myfunc()
