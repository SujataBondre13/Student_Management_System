from Fee_Obj import Fee
from tabulate import tabulate
from exception import InvalidInputError
from operator import itemgetter


import os

class AdminManagement:
    def addStudent(student):
        with open("AdminData.txt", "a") as fp:
            fp.write(str(student))
            fp.write("\n")

    def display():
        heading = ['Roll no' ,'Name' ,'Branch' ,'Total Fee', 'Paid Fee', 'Remaining Fee']
        l1= []
        if(os.path.exists("AdminData.txt")):
            with open("AdminData.txt", "r") as fp:
                for e in fp:
                    e = e.split(",")

                    # print(e)

                    l1.append(e)
                # print(l1)
                a = sorted(l1, key=itemgetter(0))
                # print(a)

                
                a.insert(0, heading)
                # print(a)

                print(tabulate(a, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print("File not found")

    def searchByRollNo(rollNo):
        if(os.path.exists("AdminData.txt")):
            with open("AdminData.txt", "r") as fp:
               
                for e in fp:
                    try:
                        e.index(str(rollNo), 0, 4)
                    except ValueError:
                        pass
                    else:
                        print("Record found")
                        print(e)
                        StudentManagement.tableForm(e)
                        break
                else:
                    print("Record Not Found")
         
        else:
            print("File not found")

    def searchByName(name):
        if(os.path.exists("AdminData.txt")):
            with open("AdminData.txt", "r") as fp:
                for e in fp:
                    if(name in e):
                        print("Record found")
                        print(e)
                        StudentManagement.tableForm(e)
                        break
                else:
                    print("Record not found")
        else:
            print("File not found")

    def updateByRollNo(rollNo):
        if(os.path.exists("AdminData.txt")):
            isfound = False
            allStudent = [ ]
            with open("AdminData.txt", "r") as fp:
                for e in fp:
                    try:
                        e.index(str(rollNo), 0, 4)
                    except ValueError:
                        # allStudent.append(e)
                        pass
                    else:
                        e = e.split(",")
                        while 1:
                            try:
                                answer = input("Do u want to change Rollno(yes/no): ")
                                if(answer == 'yes' or answer == 'no'):
                                    answer
                                    break
                                else:
                                    raise InvalidInputError
                            except InvalidInputError:
                                print("Please Enter answer as 'yes' or 'no!")
                        
                        if(answer == "yes"):
                            new_RollNo = int(input("Enter new_RollNo: "))
                            e[0] = str(new_RollNo)

                        while 1:
                            try:
                                answer = input("Do u want to change Name(yes/no): ")
                                if(answer == 'yes' or answer == 'no'):
                                    answer
                                    break
                                else:
                                    raise InvalidInputError
                            except InvalidInputError:
                                print("Please Enter answer as 'yes' or 'no!")
                        
                        if(answer == "yes"):
                            new_Name = input("Enter new_Name: ")
                            e[1] = new_Name

                        while 1:
                            try:
                                answer = input("Do u want to change Branch(yes/no): ")
                                if(answer == 'yes' or answer == 'no'):
                                    answer
                                    break
                                else:
                                    raise InvalidInputError
                            except InvalidInputError:
                                print("Please Enter answer as 'yes' or 'no!")
                        
                        if(answer == "yes"):
                            new_Branch = input("Enter new_Name: ")
                            e[2] = new_Branch                            


                        e = ",".join(e)
                        # allStudent.append(e)
                        isfound = True

                    finally:
                        allStudent.append(e)

            if(isfound == True):
                with open("AdminData.txt", "w") as fp:  #open in w mode bkz old data will get deleted and data in allStudent will write in file
                    for e in allStudent:
                        fp.write(e)

            else:
                print("Record not found")
        else:
            print("File not found")

    def deleteByRollNo(rollNo):
        if(os.path.exists("AdminData.txt")):
            isfound = False
            allStudent = [ ]
            with open("AdminData.txt", "r") as fp:
                for emp in fp:
                    try:
                        #check if id is present
                        emp.index(str(rollNo), 0, 4)
                    except ValueError:
                        # if not then copy record to allStudent container
                        allStudent.append(emp)
                    else:
                        # record found need to delete
                        isfound = True
            if(isfound == True):
                with open("AdminData.txt", "w") as fp:  #open in w mode bkz old data will get deleted and data in allStudent will write in file
                    for e in allStudent:
                        fp.write(e)

            else:
                print("Record not found")
        else:
            print("File not found")



class StudentManagement():

    def showRecord(rollNo):
        if(os.path.exists("AdminData.txt")):
            with open("AdminData.txt", "r") as fp:
            
                for a in fp:
                    try:
                        a.index(str(rollNo), 0, 4)
                    except ValueError:
                        pass
                    else:
                        print("Record found")
                        # print(e)
                        StudentManagement.tableForm(a)
                        break                                  
                else:
                    print("Record Not Found")   
        else:
            print("File not found")

    def tableForm(a):
        header = ['Roll no' ,'Name' ,'Branch' ,'Total Fee', 'Paid Fee', 'Remaining Fee']
        list1= []

        a = a.split(",")
        # print(a)
        list1.append(list(a))     
        list1.insert(0, header)
        # print(list1)

        print(tabulate(list1, headers='firstrow', tablefmt='fancy_grid'))

        if(eval(a[4]) == 5000):
            print("First Installment Completed!")
        elif(eval(a[4]) == 8000):
            print("Second Installment Completed!")
        elif(eval(a[4]) == 10000):
            print("Full Fee Done!!!")

    def payFee(rollNo):
            if(os.path.exists("AdminData.txt")):
                isfound = False
                allfee = [ ]
                with open("AdminData.txt", "r") as fp:
                    for e in fp:
                        try:
                            e.index(str(rollNo), 0, 4)
                        except ValueError:
                            # allStudent.append(e)
                            pass
                        else:
                            e = e.split(",")
                            print("Three Installments Available 1st- 5000, 2nd- 3000, 3rd- 2000")
                            if(eval(e[4]) == 5000):
                                print("Your First Installment Completed!")
                            elif(eval(e[4]) == 8000):
                                print("Your Second Installment Completed!")
                            elif(eval(e[4]) == 10000):
                                print("Full Fee Done!!!")
                            while 1:
                                try:
                                    amount = int(input("Enter Amount to pay fee(): "))
                                except ValueError:
                                    print("Enter numbers only!")
                                else:
                                    amount
                                    break

                            total = eval(e[3])
                            paid = eval(e[4])
                             
                            newpaid = paid + amount
                            e[4] = str(newpaid)
                        
                            newremain = total - newpaid
                            e[5] = str(newremain)

                            e[3] = str(total)

                            e = ",".join(e)
                            # allfee.append(e)
                            isfound = True

                        finally:
                            allfee.append(e)

                if(isfound == True):
                    with open("AdminData.txt", "w") as fp:  #open in w mode bkz old data will get deleted and data in allStudent will write in file
                        for e in allfee:
                            fp.write(e)
                            fp.write("\n")
                else:
                    print("Record not found")
            else:
                print("File not found")



        # with open("StudentData.txt", "a") as fp:
        #     fp.write(str(e))
        #     fp.write("\n")

