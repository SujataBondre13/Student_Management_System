from Menu_Page import Menu


class Login():
    def Admin_Login():
        i = 1
        while(i < 4):
            print("\nAdmin Login: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if(username == "Admin" and password == "Admin@123"):
                Menu.Admin_Menu()
                break

            else:
                print("Wrong Credentials!!")
                i += 1



    def Student_Login():
        j = 1
        while(j < 4):
            print("\nStudent Login: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if(username == "Student" and password == "Student@123"):
                Menu.Student_Menu()
                break
            else:
                print("Wrong Credentials!!")
                j += 1