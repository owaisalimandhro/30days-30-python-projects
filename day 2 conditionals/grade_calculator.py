marks = int(input("Enter your marks to check the grade: "))
if marks >= 80:
    print("you have got a A grade")
elif marks <=79& marks>=60:
    print("you have got a B grade")
elif marks <=59 & marks>=40:
    print("you have unforunately secured c grade")
elif marks <40:
    print("you have failed ")
else:
    print("invalid input enter again")