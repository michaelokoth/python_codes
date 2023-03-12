#programme to check bonus
salary=int(input("enter salary paid:"))
years=int(input("Enter number of years worked:"))
if years >10:
    bonus=0.1*salary
    print(" net bonus is:",bonus)
elif years >=6 and years <=10:
    bonus=0.08*salary
    print("net bonus is:",bonus)
elif years <6:
    bonus=0.05*salary
    print("net bonus is:",bonus)