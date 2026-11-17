email = "xyz@gmail.com"
password = "xyzpassword"
user_email = input("Enter email to login: ")
user_password = input("Enter password to login: ")
if user_email == email and user_password == password:
    print("Successful login ,welcome and hello")
elif user_email != email or user_password != password:
    print("wrong credentials , retinvalid input retry again")
else:
    print("invalid input")