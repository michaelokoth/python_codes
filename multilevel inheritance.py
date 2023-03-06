#program for inheritance
class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog:
    def bark(self):
        print("I can bark")
class cow:
    def mows(self):
        print("I can mow")
class baby(Animal,Dog,cow):
    def feeds(self):
        print("I can feed")
b=baby()
b.legs()
b.fur()
b.bark()
b.mows()
b.feeds()