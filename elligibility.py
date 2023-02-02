#vote elligibility
countries=["kenya","uganda","tanzania"]
country=input("Enter country:").lower()
age=int(input("Enter age:"))
if country in countries and age>=18:
    print("Eligible to vote")
else:
    print("not elligible to vote")