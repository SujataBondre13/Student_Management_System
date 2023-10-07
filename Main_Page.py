
from Login_Page import Login

if(__name__ == "__main__"):
    while 1:
        print("\nWelcome to Student Management System")
        print(" ")
        print("1. Login as Admin")
        print("2. Login as Student")

        while 1:
            try:
                choice = int(input("Enter Choice: "))
            except ValueError:
                print("Please Enter Numbers Only!")
            else:
                choice
                break
        
        if(choice == 1):
            Login.Admin_Login()

        elif(choice == 2):
            Login.Student_Login()
        else:
            print("Wrong Choice!")
