from Management_Page import AdminManagement, StudentManagement
from Object_Page import StudentObject
import os

class Menu():

    def Admin_Menu():
        while 1:
            print("\nAdmin Menu: ")
            print("1. Add Student")
            print("2. Display Students Record")
            print("3. Search Existing Student")
            print("4. Update Existing Student")
            print("5. Delete Existing Student")
            print("6. Exit")

            while 1:
                try:
                    admin_Option = int(input("\nEnter Option: "))
                except ValueError:
                    print("Please Enter Numbers Only!")
                else:
                    admin_Option
                    break

            # if(admin_Option == 1):
            #     while 1:
            #         try:
            #             rollNo = int(input("Enter RollNo: "))
            #             if(len(str(rollNo)) == 3):
            #                 # rollNo    
            #                 break
            #             else:
            #                 raise ValueError
                        
            #         except ValueError:
            #             print("Please Enter 3 Digit Number Only!")

            if(admin_Option == 1):
                with open("AdminData.txt", "a") as fp:
                    while 1:
                        try:
                            rollNo = int(input("\nEnter RollNo: "))
                            if(len(str(rollNo)) == 3):
                                rollNo
                                if(os.path.exists("AdminData.txt")):
                                    with open("AdminData.txt", "r") as fp:
                                        for e in fp:
                                            try:
                                                e.index(str(rollNo), 0, 4)
                                            except ValueError:
                                                pass
                                            else:
                                                print("Already Exist")
                                                # print(e)
                                                break
                                        else:
                                            rollNo
                                            break

                            else:
                                raise ValueError
                                
                        except ValueError:
                            print("Please Enter 3 digit Roll Number")
                             

                while 1:
                    try:        
                        name = input("Enter Name: ")
                        if(name != '' and all(chr.isalpha() or chr.isspace() for chr in name)):
                            name
                            break
                        else:
                            raise TypeError
                    
                    except TypeError:
                        print("Please Enter Letters Only!")
                        
                while 1:
                    try:
                        branch = input("Enter Branch: ")
                        if branch.isalpha():
                            branch
                            break
                        else:
                            raise TypeError
                    
                    except TypeError:
                        print("Please Enter Letters Only!")
                        
                total_fees = 10000

                print("Three Installments Available 1st- 5000, 2nd- 3000, 3rd- 2000")
                while 1:
                    try:    
                        amount = int(input("Enter Amount to pay: "))
                    except ValueError:
                        print("Please Enter Numbers Only!")
                    else:
                        amount
                        break

                remain = total_fees - amount
                
                student = StudentObject(rollNo, name, branch, total_fees, amount, remain)
                AdminManagement.addStudent(student)


            elif(admin_Option == 2):
                AdminManagement.display()

            elif(admin_Option == 3):
                print("Select the search criteria: ")
                print("1. Roll No")
                print("2. Name")

                while 1:
                    try:
                        choice = int(input("Enter Choice: "))
                    except ValueError:
                        print("Please Enter Numbers Only!")
                    else:
                        choice
                        break
                
                if(choice == 1):
                    while 1:      
                        try:
                            rollNo = int(input("\nEnter RollNo to Search: "))
                        except ValueError:
                            print("Please Enter Numbers Only!")
                        else:
                            rollNo
                            break
                    AdminManagement.searchByRollNo(rollNo)

                elif(choice == 2):
                    while 1:
                        try:        
                            name = input("Enter Name to Search: ")
                            if name.isalpha():
                                name
                                break
                            else:
                                raise TypeError
                    
                        except TypeError:
                            print("Please Enter Letters Only!")
                    AdminManagement.searchByName(name)

                else:
                    print("Wrong Choice")




            elif(admin_Option == 4):
                while 1:
                    try:
                        rollNo = int(input("\nEnter RollNo to Update: "))
                    except ValueError:
                        print("Please Enter Numbers Only!")
                    else:
                        rollNo
                        break
                AdminManagement.updateByRollNo(rollNo)

            elif(admin_Option == 5):
                while 1:
                    try:
                        rollNo = int(input("\nEnter RollNo to Delete: "))
                    except ValueError:
                        print("Please Enter Numbers Only!")
                    else:
                        rollNo
                        break
                AdminManagement.deleteByRollNo(rollNo)

            elif(admin_Option == 6):
                break

            else:
                print("No valid option selected")



            
    def Student_Menu():
        while 1:
            print("\nStudent Menu: ")
            print("1. Display Your Record")
            print("2. Pay Fee")
            print("3. Exit")

            while 1:
                try:
                    student_Option = int(input("\nEnter Option: "))
                except ValueError:
                    print("Please Enter Numbers Only!")
                else:
                    student_Option
                    break

            if(student_Option == 1):
                while 1:
                    try:
                        rollNo = int(input("\nEnter your Roll Number: "))
                    except ValueError:
                        print("Please Enter Numbers Only!")
                    else:
                        rollNo
                        break
                StudentManagement.showRecord(rollNo)

            elif(student_Option == 2):
                while 1:
                    try:
                        rollNo = int(input("\nEnter Roll No. to pay Fee: "))
                    except ValueError:
                        print("Please Enter Numbers Only!")
                    else:
                        rollNo
                        break
                StudentManagement.payFee(rollNo)

            elif(student_Option == 3):
                break





























