num1= int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
num3 = int(input("enter your third number: "))

if num1>num2 and num1 > num3:
    print("first num  is greatest of all three num ")
elif num2>num1 and num2> num3:
    print("second number is greatest of all three num")
elif num3> num1 and num3>num2:
    print("third number is greatest of all three num")
else:
    print("all 3 of numbers are equal")