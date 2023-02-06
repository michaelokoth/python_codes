#programme to print largest number
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if (num1>num2 and num1>num3):
    print("one is greatest")
elif (num2>num1 and num2>num3):
    print("two is greatest")
elif (num3>num1 and num3>num2):
    print("three is the greatest")