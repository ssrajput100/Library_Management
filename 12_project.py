#this program is build to manage the the stock and lending of books from the library of an institute
from colorama import Fore,Back,Style
import colorama
colorama.init()
print(Fore.RED)
print("_"*99)
print("     | WELCOME   TO   THE   LIBRARY   OF   DELHI   PUBLIC   SCHOOL,  RISALI | ")
print("_"*99)
print("                                 *MAIN MENU*                          ")
print(Fore.CYAN)
print("_"*99)
print("PRESS  1  TO SEE THE STUDENT TABLE.")  
print("PRESS  2  TO MODIFY THE STUDENT TABLE.")
print("PRESS  3  TO SEE THE STAFF TABLE.")
print("PRESS  4  TO MODIFY THE STAFF TABLE.")
print("PRESS  5  TO SEE THE BOOKS TABLE.")
print("PRESS  6  TO MODIFY THE BOOKS TABLE.")
print("PRESS  7  TO SEE THE ISSUED BOOKS TABLE.")
print("PRESS  8  FOR ISSUING A BOOK FROM LIBRARY.")
print("PRESS  9  TO SEE THE RECOMMENDED BOOKS TABLE.")
print("PRESS  10 FOR RECOMMENDING BOOKS TO THE LIBRARY.")
print("PRESS  11 TO SEE THE RETURNED BOOKS TABLE.")
print("PRESS  12 FOR RETURNING AN ISSUED BOOK TO THE LIBRARY.")
print("_"*99)

#this function retrieves records from student_table of mysql and displays it in tabular form
def student_table_display():
    import pymysql as pym
    #mycon is used as connection object everywhere
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute ('select * from STUDENT_TABLE')
    data=cursor.fetchall()
    print (Fore.MAGENTA)
    print ('-'*99)
    print ('                                        STUDENT    DETAILS   ')
    print ('-'*99)
    print ('STUDENT_ID   ','   STUDENT_NAME','        CLASS','   SECTION','     CONTACT','        GENDER','   DATE_OF_BIRTH')
    print('-'*99)
    for row in data:
            Student_ID,Student_Name,Class,Section,Contact,Gender,Date_Of_Birth=row
            print (Fore.YELLOW+'{:<10s}       {:<15s}       {:<2d}        {:<1s}        {:<11d}        {:>1s}        {:}'. format (Student_ID,Student_Name,Class,Section,Contact,Gender,Date_Of_Birth))
    print ('-'*99)
    mycon.close()
    
#this function deals with the changes which the user wants to make in the student_table
def student_table_modify():
    print(Fore.GREEN)
    print("                            *SUB MENU*  ")
    print("->ENTER 1 FOR ADDING A RECORD IN STUDENT TABLE")
    print("->ENTER 2 FOR DELETING A RECORD IN STUDENT TABLE")
    print("->ENTER 3 FOR CHANGING THE DETAILS OF A RECORD IN STUDENT TABLE")
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("ENTER THE DETAILS OF THE NEW STUDENT :-")
        Student_ID=input("ENTER THE STUDENT ID (IT HAS TO BE 6 CHARACTERED WITH 1 LETTER IN THE START FOLLOWED BY 5 DIGITS) :")
        Student_Name=input("ENTER THE STUDENT NAME :")
        Class=input("ENTER THE STUDENT CLASS :")
        Section=input("ENTER THE STUDENT SECTION :")
        Contact=input("ENTER THE STUDENT CONTACT :")
        Gender=input("ENTER THE GENDER OF THE STUDENT:")
        Date_Of_Birth=input("ENTER THE STUDENT DATE OF BIRTH :")
        print ('-'*90)
        mysql_insert_query = "INSERT INTO STUDENT_TABLE VALUES (%s, %s, %s, %s,%s,%s,%s) "
        recordTuple=(Student_ID,Student_Name,Class,Section,Contact,Gender,Date_Of_Birth)
        cursor.execute(mysql_insert_query,recordTuple)
        mycon.commit()
        print ('-'*90)
        print("Record inserted successfully into STUDENT table.")
    elif choice==2:
        Student_ID=input("ENTER THE ID OF THE  STUDENT TO BE REMOVED  :-")
        print("Displaying Record Of The Removed Student Before Deleting It:")
        sql_select_query="select * from Student_Table where Student_ID='{}'".format(Student_ID)
        cursor.execute(sql_select_query)
        record=cursor.fetchall()
        print(record)
        print ('-'*90)
        sql_Delete_query = "Delete from STUDENT_TABLE where Student_ID = '{}'".format(Student_ID)
        cursor.execute(sql_Delete_query)
        mycon.commit()
        print("Record deleted successfully!")
        print('-'*90)
    elif choice==3:
        Student_ID=input("ENTER ID OF THE STUDENT, WHOSE DETAILS YOU WANT TO UPDATE IN THE STUDENT TABLE :")
        print("Before updating the record:")
        sql_select_query = "select * from STUDENT_TABLE where Student_ID='{}'".format(Student_ID)
        cursor.execute(sql_select_query)
        record=cursor.fetchall()
        print(record)
        print ('-'*90)
        print("ENTER A NO. ACCORDING TO WHAT DETAIL YOU WANT TO UPDATE OF THE STUDENT !")
        print("->ENTER 1 FOR UPDATING THE STUDENT NAME")
        print("->ENTER 2 FOR UPDATING THE STUDENT CONTACT")
        Choice=int(input("ENTER YOUR CHOICE :"))
        if Choice==1:
            Student_Name=input("ENTER NEW NAME OF THE STUDENT :")
            sql_update_query = "Update STUDENT_TABLE set Student_Name='{}' where Student_ID='{}'".format(Student_Name,Student_ID)
            cursor.execute(sql_update_query)
            mycon.commit()
            print ('-'*90)
            print("Record updated successfully!")
            print ('-'*90)
            print("Updated record:")
            cursor.execute(sql_select_query)
            record=cursor.fetchall()
            print(record)
            print ('-'*90)
        elif Choice==2:
            Contact=int(input("ENTER THE NEW CONTACT OF THE STUDENT :"))
            sql_update_query = "Update STUDENT_TABLE set Contact='{}' where Student_ID='{}'".format(Contact,Student_ID)
            cursor.execute(sql_update_query)
            mycon.commit()
            print("Record Updated successfully ")
            print ('-'*90)
            print("Updated record:")
            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            print(record)
            print ('-'*90)
        else:
            print("Please enter no. out of given options !")
    else:
        print("Please enter no. out of given options !")
    mycon.close()

#this function retrieves records from staff_details of mysql and displays it in tabular form
def staff_table_display():
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute ('select * from Staff_Details')
    data=cursor.fetchall()
    print (Fore.MAGENTA)
    print ('-'*144)
    print ('                                                             STAFF    DETAILS   ')
    print ('-'*144)
    print ('STAFF_ID ','          STAFF_NAME','                        POST','                           CONTACT','         GENDER   ','   HIREDATE','         SALARY')
    print('-'*144)
    for row in data:
            Staff_ID,Staff_Name,Post,Contact,Gender,Hire_Date,Salary_in_Rs=row
            print (Fore.YELLOW+'{:<10s}          {:<25s}          {:<20s}           {:<12d}        {:<5s}     {:}    {:>10d}'. format (Staff_ID,Staff_Name,Post,Contact,Gender,Hire_Date,Salary_in_Rs))
    print ('-'*144)
    mycon.close() 

#this function deals with the changes which the user wants to make in the staff_details
def staff_table_modify():
    print(Fore.GREEN)
    print("                         SUB  MENU                                       ")
    print("->ENTER 1 FOR ADDING A RECORD IN STAFF TABLE")
    print("->ENTER 2 FOR DELETING A RECORD IN STAFF TABLE")
    print("->ENTER 3 FOR CHANGING THE DETAILS OF A RECORD IN STAFF TABLE")
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("ENTER THE DETAILS OF THE NEW STAFF MEMBER :-")
        STAFF_ID_=input("ENTER THE STAFF ID (IT HAS TO BE 6 CHARACTERED WITH 2 LETTERS IN THE START FOLLOWED BY 4 DIGITS) :")
        STAFF_NAME_=input("ENTER THE STAFF NAME :")
        POST_=input("ENTER THE STAFF POST :")
        CONTACT_=input("ENTER THE STAFFCONTACT :")
        GENDER_=input("ENTER THE GENDER OF THE STAFF(F/M):")
        HIRE_DATE_=input("ENTER THE STAFF HIRE DATE :")
        SALARY_=input("ENTER THE STAFF SALARY IN RS:")
        print ('-'*99)
        mysql_insert_query="INSERT INTO Staff_Details  VALUES (%s, %s, %s, %s,%s,%s,%s)"
        recordTuple=(STAFF_ID_,STAFF_NAME_,POST_,CONTACT_,GENDER_,HIRE_DATE_,SALARY_)
        cursor.execute(mysql_insert_query,recordTuple)
        mycon.commit()
        print ('-'*99)
        print("Record inserted successfully into staff table.")
    elif choice==2:
        STAFF_ID=input("ENTER THE STAFF ID OF THE  STAFF MEMBER TO BE REMOVED  :-")
        print("Displaying Staff Record Of The Removed Member Before Deleting It")
        sql_select_query = "select * from Staff_Details where STAFF_ID ='{}'".format(STAFF_ID)
        cursor.execute(sql_select_query)
        record=cursor.fetchall()
        print(record)
        print ('-'*99)
        sql_Delete_query = "Delete from Staff_Details where STAFF_ID ='{}'".format(STAFF_ID)
        cursor.execute(sql_Delete_query)
        mycon.commit()
        cursor.execute(sql_select_query)
        print("Record Deleted successfully!")
    elif choice==3:
        STAFF_ID=input("ENTER ID OF THE STAFF, WHOSE DETAILS YOU WANT TO UPDATE IN THE STAFF TABLE :")
        print("Before updating the record:")
        sql_select_query = "select * from Staff_Details where STAFF_ID ='{}'".format(STAFF_ID)
        cursor.execute(sql_select_query)
        record=cursor.fetchall()
        print(record)
        print ('-'*99)
        print("SELECT A NO. ACCORDING TO WHAT DETAIL YOU WANT TO UPDATE OF THE STAFF MEMBER !")
        print("->SELECT 1 FOR UPDATING THE STAFF NAME")
        print("->SELECT 2 FOR UPDATING THE POST")
        print("->SELECT 3 FOR UPDATING THE CONTACT")
        print("->SELECT 4 FOR UPDATING THE SALARY")
        Choice=int(input("ENTER YOUR CHOICE :"))
        print ('-'*99)
        if Choice==1:
            STAFF_NAME=input("ENTER THE UPDATED NAME OF STAFF MEMBER :")
            sql_update_query="Update Staff_Details set STAFF_NAME='{}' where STAFF_ID='{}'".format(STAFF_NAME,STAFF_ID)
            cursor.execute(sql_update_query)
            mycon.commit()
            print ('-'*99)
            print("Record Updated successfully!")
            print ('-'*99)
            print("After updating record:")
            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            print(record)
            print ('-'*99)
        elif Choice==2:
            POST=input("ENTER THE NEW POST OF THE STAFF MEMBER :")
            sql_update_query = "Update Staff_Details set POST='{}' where STAFF_ID ='{}'".format(POST,STAFF_ID)
            print ('-'*99)
            cursor.execute(sql_update_query)
            print ('-'*99)
            mycon.commit()
            print("Record Updated successfully!")
            print("After updating record:")
            cursor.execute(sql_select_query)
            record=cursor.fetchall()
            print(record)
            print ('-'*99)
        elif Choice==3:
            Contact=input("ENTER THE NEW CONTACT OF THE STAFF MEMBER :")
            sql_update_query = "Update Staff_Details set Contact='{}' where STAFF_ID = '{}'".format(Contact,STAFF_ID)
            print ('-'*99)
            cursor.execute(sql_update_query)
            print ('-'*99)
            mycon.commit()
            print("Record Updated successfully!")
            print("After updating record:")
            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            print(record)
            print ('-'*99)
        elif Choice==4:
            Salary_in_Rs=int(input("ENTER THE NEW SALARY OF THE STAFF MEMBER :"))
            sql_update_query = "Update Staff_Details set Salary_in_Rs='{}' where STAFF_ID = '{}'".format(Salary_in_Rs,STAFF_ID )
            print ('-'*99)
            cursor.execute(sql_update_query)
            mycon.commit()
            print ('-'*99)
            print("Record Updated successfully!")
            print ('-'*99)
            print("After updating record:")
            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            print(record)
            print ('-'*99)
        else:
            print("Please enter no. out of given options !")
    else:
            print("Please enter no. out of given options !")

    mycon.close()

#this function retrieves records from books_table of mysql and displays it in tabular form
def book_table_display():
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon. cursor()
    cursor.execute ('select * from Books')
    data=cursor.fetchall()
    print (Fore.MAGENTA)
    print ('-'*169)
    print ('                                                                   LIBRARY    BOOK    DETAILS   ')
    print ('-'*169)
    print ('BOOK_ID   ','        BOOK_NAME            ','               AUTHOR                            ','PUBLISHER                    ','   SUBJECT            ','   CLASS_GROUP','  LANGUAGE')
    print('-'*169)
    for row in data:
        Book_ID,Book_Name,Author,Publisher,Subject,Class_Group,Language=row
        print (Fore.YELLOW+'{:<10s}          {:<25s}          {:<25s}           {:<25s}        {:<20s}     {:<8s}    {:<10s}'. format (Book_ID,Book_Name,Author,Publisher,Subject,Class_Group,Language))
    print ('-'*169)
    mycon.close()

#this function deals with the changes which the user wants to make in the books_table
def book_table_modify():
    print(Fore.GREEN)
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    print("                              SUB MENU  ")
    print("->ENTER 1 FOR ADDING A RECORD IN BOOK TABLE")
    print("->ENTER 2 FOR DELETING A RECORD IN BOOK TABLE")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("ENTER THE DETAILS OF THE NEW BOOK :-")
        BOOK_ID=input("ENTER THE BOOK ID (IT HAS TO BE 6 CHARACTERED WITH A CAPITAL LETTER IN THE START FOLLOWED BY 4 DIGITS FOLLOWED BY A CAPITAL LETTER) :")
        BOOK_NAME=input("ENTER THE BOOK NAME :")
        AUTHOR=input("ENTER THE AUTHOR OF THE BOOK :")
        PUBLISHER=input("ENTER THE PUBLISHER OF THE BOOK :")
        SUBJECT=input("ENTER THE SUBJECT OF THE BOOK :")
        CLASS_GROUP=input("ENTER THE CLASS GROUP OF THE BOOK:")
        LANGUAGE=input("ENTER THE LANGUAGE OF THE BOOK :")
        print ('-'*99)
        mysql_insert_query = "INSERT INTO BOOKS VALUES (%s, %s, %s, %s,%s,%s,%s) "
        recordTuple = (BOOK_ID,BOOK_NAME,AUTHOR,PUBLISHER,SUBJECT,CLASS_GROUP,LANGUAGE)
        cursor.execute(mysql_insert_query,recordTuple)
        mycon.commit()
        print('-'*99)
        print("Record inserted successfully into BOOK table.")
    elif choice==2:
        Book_ID=input("ENTER THE ID OF THE  BOOK TO BE REMOVED FROM THE BOOK LIST :-")
        print("Displaying Record Of The Removed BOOK Before Deleting It")
        sql_select_query = "select * from Books where Book_ID ='{}'".format(Book_ID)
        cursor.execute(sql_select_query)
        record=cursor.fetchall()
        print(record)
        print ('-'*99)
        sql_Delete_query = "Delete from Books where Book_ID ='{}'".format(Book_ID)
        cursor.execute(sql_Delete_query)
        mycon.commit()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print ('-'*99)
        print("Record Deleted successfully!")
    else:
        print("Please enter no. out of given options !")
    mycon.close()

#this function retrieves records from issued_book_table of mysql and displays it in tabular form
def issued_book_table_display():
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute ('select * from ISSUED_BOOKS')
    data=cursor.fetchall()
    print (Fore.MAGENTA)
    print ('-'*169)
    print ('                                                          LIBRARY   ISSUED    BOOK    DETAILS')
    print ('-'*169)
    print ('Book_ID   ','         Book_Name','                         Student_ID','          Student_Name','                   Class','    Section','      Issued_Date','    Last_Return_Date')
    print('-'*169)
    for row in data:
        Book_ID,Book_Name,Student_ID,Student_Name,Class,Section,Issued_Date,Last_Return_Date=row
        print (Fore.YELLOW+'{:<10s}          {:<25s}          {:<10s}           {:<25s}        {:<7d}     {:<7s}    {:}      {:}'. format (Book_ID,Book_Name,Student_ID,Student_Name,Class,Section,Issued_Date,Last_Return_Date))
    print ('-'*169)
    mycon.close()

#this function allows the issuing of books from library to user under certain conditions and entries the record
def issuing_book():
    import pymysql as pym
    print(Fore.LIGHTRED_EX)
    S_ID=input("Enter Student_ID:")
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute("select * from Student_Table")
    data=cursor.fetchall()
    records=cursor.rowcount
    for i in range(0,records):
        if data[i][0]==S_ID:
            mycon=pym.connect("localhost","root","sejalb","students")
            cursor=mycon.cursor()
            cursor.execute("select * from Issued_Books")
            datas=cursor.fetchall()
            records=cursor.rowcount
            for j in range(0,records):
                if datas[j][2]==S_ID:
                    print("First return the previous book!")
                    break
            else:
                B_ID=input("Enter Book_ID:")
                mycon=pym.connect("localhost","root","sejalb","students")
                cursor=mycon.cursor()
                cursor.execute("select * from Books")
                datum=cursor.fetchall()
                records=cursor.rowcount
                for k in range(0,records):
                    if datum[k][0]==B_ID:
                        print("Book is found in Library Stock.")
            
                        mycon=pym.connect("localhost","root","sejalb","students")
                        cursor=mycon.cursor()
                        cursor.execute("select * from Issued_Books")
                        dat=cursor.fetchall()
                        records=cursor.rowcount
                        for l in range(0,records):
                            if dat[l][0]==B_ID:
                                print("Sorry,the book is already Issued...")
                                break
                        else:
                            print("Book is available for Issuing.")
                            Q="insert into issued_books(Book_ID,Book_Name,Student_ID,Student_Name,Class,Section) values(%s, %s, %s, %s,%s,%s)"
                            rec=(B_ID,datum[k][1],S_ID,data[i][1],data[i][2],data[i][3])
                            cursor.execute(Q,rec)
                            mycon.commit()
                            query="update issued_books set Issued_Date= curdate() where Book_ID='{}'".format(B_ID)
                            cursor.execute(query)
                            mycon.commit()
                            Query="update issued_books set Last_Return_Date=ISSUED_DATE+7 where Book_ID='{}'".format(B_ID)
                            cursor.execute(Query)
                            mycon.commit()
                            print("Book is issued and record is added successfully!")
                            print("Thank you for issuing book. Please visit again! ")
                        break
                else:
                    print("Invalid Book_ID!")
                break
            break         
    else:
        print("Invalid Student_ID!")
            
    mycon.close()

#this function retrieves records from recommended_book_table of mysql and displays it in tabular form
def recommended_book_table_display():
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute('select * from recommended_books')
    data=cursor.fetchall()
    print (Fore.MAGENTA)
    print ('-'*115)
    print ('                          LIBRARY    RECOMMENDED    BOOK    DETAILS')
    print ('-'*115)
    print ('Student_ID','      Student_Name','           Class','     Section','   Book_Name','                   Author')
    print('-'*115)
    for row in data:
            Student_Name,Student_ID,Class,Section,Book_Name,Author=row
            print (Fore.YELLOW+'{:<10s}       {:<20s}    {:<2d}          {:<2s}        {:<25s}     {:<25s}'. format(Student_Name,Student_ID,Class,Section,Book_Name,Author))
            
    print ('-'*115)
    mycon.close()

#this function enables user to to recommend any book he/she wishes which isn't present in the libray
def recommending_book():
    import pymysql as pym
    print(Fore.LIGHTRED_EX)
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    S_ID=input("Enter Student_ID:")
    cursor.execute("select * from Student_Table")
    data=cursor.fetchall()
    records=cursor.rowcount
    for i in range(0,records):
        if data[i][0]==S_ID:
            Student_Name=input("ENTER THE STUDENT NAME :")
            Class=input("ENTER THE STUDENT CLASS :")
            Section=input("ENTER THE STUDENT SECTION :")
            Book_Name=input("ENTER THE BOOK NAME :")
            Author=input("ENTER THE AUTHOR NAME :")
            mysql_insert_query="INSERT INTO Recommended_Books VALUES (%s, %s, %s, %s,%s,%s)"
            recordTuple=(S_ID,Student_Name,Class,Section,Book_Name,Author)
            cursor.execute(mysql_insert_query,recordTuple)
            mycon.commit()
            break
    else:
        print("invalid student_ID")
    mycon.close() 

#this function retrieves records from returned_book_table of mysql and displays it in tabular form
def returned_books_table_display():
    import pymysql as pym
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute('select * from returned_books')
    data=cursor.fetchall()
    print (Fore.MAGENTA)
    print ('-'*145)
    print ('                                                 RETURNED   BOOKS    DETAILS')
    print ('-'*145)
    print ('Book_ID','          Book_Name','               Student_ID','      Student_Name','              Class','  Section','  Issue_Date','      Return_Date','   Penalty')
    print('-'*145)
    for row in data:
            Book_ID,Book_Name,Student_ID,Student_Name,Class,Section,Issue_Date,Return_Date,Penalty=row
            print (Fore.YELLOW+'{:<10s}        {:<15s}          {:<10s}       {:<17s}          {:<2d}      {:>2s}        {:}       {:}     {:<10s}'. format(Book_ID,Book_Name,Student_ID,Student_Name,Class,Section,Issue_Date,Return_Date,Penalty))
    print ('-'*145)
    mycon.close()

#this function entries record when a user returns any book and checks if he/she is charged with penalty
def returning_book():
    import pymysql as pym
    print(Fore.LIGHTRED_EX)
    S_ID=input("Enter Student_ID:")
    mycon=pym.connect("localhost","root","sejalb","students")
    cursor=mycon.cursor()
    cursor.execute("select * from Student_Table")
    data=cursor.fetchall()
    records=cursor.rowcount
    for i in range(0,records):
        if data[i][0]==S_ID:
            B_ID=input("Enter Book_ID:")
            mycon=pym.connect("localhost","root","sejalb","students")
            cursor=mycon.cursor()
            cursor.execute("select * from Issued_Books")
            dat=cursor.fetchall()
            records=cursor.rowcount
            for l in range(0,records):
                if dat[l][0]==B_ID and dat[l][2]==S_ID:
                    Q="insert into returned_books(Book_ID,Book_Name,Student_ID,Student_Name,Class,Section,Issue_Date) values(%s, %s, %s, %s,%s,%s,%s)"
                    rec=(B_ID,dat[l][1],S_ID,dat[l][3],dat[l][4],dat[l][5],dat[l][6])
                    cursor.execute(Q,rec)
                    mycon.commit()
                    query="update returned_books set Return_Date=curdate() where Book_ID='{}'".format(B_ID)
                    cursor.execute(query)
                    mycon.commit()
                    Query="update returned_books set Penalty=datediff(Return_Date,Issue_Date)*50 where Book_ID='{}'".format(B_ID)
                    cursor.execute(Query)
                    mycon.commit()
                    QUery="delete from Issued_Books where Book_ID='{}'".format(B_ID)
                    cursor.execute(QUery)
                    mycon.commit()
                    print("Book is returned!")
                    print("Thank you. Please visit again!")
                    break
            else:   
                print("Invalid Book_ID")
            break
    else:
        print("Invalid Student_ID")
                    
def main_menu():
    print(Fore.CYAN)
    option=int(input("ENTER YOUR CHOICE :"))
    if option==1:
        student_table_display()
    elif option==2:
        student_table_modify()
    elif option==3:
        staff_table_display()
    elif option==4:
        staff_table_modify()
    elif option==5:
        book_table_display()
    elif option==6:
        book_table_modify()
    elif option==7:
        issued_book_table_display()
    elif option==8:
        issuing_book()
    elif option==9:
        recommended_book_table_display()
    elif option==10:
        recommending_book()
    elif option==11:
        returned_books_table_display()
    elif option==12:
        returning_book()
    else:
        print(Fore.CYAN+"Please enter no. out of given options!")

def run_program():
    ans="yes"
    while ans=="yes":
        main_menu()
        print(Fore.CYAN)
        ans=input("Do you want to run the program again? (yes/no)")
    else:
        print()
        print(Fore.RED+"                         Thankyou for using our program. Please visit again!")
        print(Fore.RED+"                                               -*-*-*-*-")
run_program()
             

    
    



