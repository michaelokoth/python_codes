#program for inheritance
class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
class cow(Animal):
    def mows(self):
        print("the cow mows")
d=Dog()
d.bark()
d.legs()
d.fur()
c=cow()
c.mows()