#A program to allow a citizen to vote
age=int(input("Enter your age:"))
nationality=(input("Enter your nationality:").lower)
if age>=18 and nationality=="kenyan":
    print("you can vote")
else:
    print("not allowed to vote")