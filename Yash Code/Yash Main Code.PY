# Library Management

# IMPORTS

import datetime

# Functions

# Wish me


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good  Morning")

    elif 12 <= hour < 18:
        print("Good Afternoon")

    else:
        print("Good Evening")


# Issue Book


def issue_book():
    s_h = open("Student.txt", "r")
    dat_com = " "  # Data to be compared
    stu_name = str(input("Enter the name of the Student who wants to issue\
    book"))
    while dat_com:
        dat_com = s_h.readline()
        dat_com = dat_com.rstrip('\n')
        if stu_name == dat_com:
            s_h.close()
            break
    else:
        print("Student not found")
        print("First, add the student then issue the book")
        exit()

    b_h = open("Book.txt", "r")
    book_name = str(input("Enter the name of the book"))
    time = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%d/%m/%y")
    while dat_com:
        dat_com = b_h.readline()
        dat_com = dat_com.rstrip('\n')
        if book_name == dat_com:
            i_h = open("Issue.txt", "a")
            rec = stu_name + "," + book_name + "," + date + "," + time + "\n"
            i_h.write(rec)
            print("Book Issued Successfully")
            break
    else:
        print("book not found")
        print("First Register the book in the Library then issue the book")


# Return Book


def return_book():
    i_h = open("Issue.txt", "r")  # opening file
    ret = " "  # Variable to keep record
    stu_name = str(input("Enter the name of the student who wants to return\
    the Book :"))
    while ret:
        ret = i_h.readline()
        ret = ret.rstrip('\n')  # Removing the newline character from end
        l_s = ret.split(",")
        if l_s[0] == stu_name:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            date = datetime.datetime.now().strftime("%d/%m/%y")
            ret = l_s[0] + "," + l_s[1] + "," + date + "," + time + "\n"
            r_h = open("Return.txt", "a")
            r_h.write(ret)
            print("Found Student")
            print(l_s[0], "has issued", l_s[1], "book on", l_s[2], "at",\
                  l_s[3])
            print(l_s[0], "has returned", l_s[1], "book on", date, "at",\
                  time)
            print("Book Returned Successfully")
            break
        else:
            pass

    else:
        print(stu_name, "has not issued any book")


# Add Student


def add_student():
    s_h = open("Student.txt", "a")
    student = str(input("Please Enter the name of the student"))
    rec = student + "\n"
    s_h.write(rec)
    print("Student added in the Library")


# Add Book


def add_book():
    b_h = open("Book.txt", "a")
    book = str(input("Please Enter the name of the book"))
    rec = book + "\n"
    b_h.write(rec)
    print("Book Registered in the Library")


# Book Details


def book_details():
    b_h = open("Book.txt", "r")
    dat = " "
    count = 0
    print("S.No.\tBook Name ")
    while dat:
        dat = b_h.readline()
        if dat == "":
            break
        count += 1
        print(count, "\t", dat, end="")


# Student Details


def student_details():
    s_h = open("Student.txt", "r")
    dat = " "
    count = 0
    print("S.No.\tStudent Name")
    while dat:
        dat = s_h.readline()
        if dat == "":
            break
        count += 1
        print(count, "\t", dat, end="")


def statistics():
    i_h = open("Issue.txt", "r")  # opening file
    print("Information of all books \"issued\" till date are:\n")
    print("Name , Book , Date , Time ")
    for var in i_h:
        var = var.rstrip('\n')
        print(var)

    r_h = open("Return.txt", "r")  # opening file
    print("\nInformation of all books \"returned\" till date are:\n")
    print("Name , Book , Date , Time ")
    for var in r_h:
        var = var.rstrip('\n')
        print(var)


print("\" \" LIBRARY MANAGEMENT PROGRAM \" \"")
print(" Welcome  \' \' User \' \'")
wish_me()
print("Things you can do with this program :")
print("1. Issue Book to a student")
print("2. Return Book from a student")
print("3. Register Student in the Library")
print("4. Add book in the Library")
print("5. See \'Book Details\'")
print("6. See \'Student Details\'")
print("7. Complete Information")
print("8. Exit")

ans = "y"
while ans == "y" or ans == "Y":
    c = int(input("Please Enter your \'Choice\' :-"))
    if c == 1:
        print("Issuing Book")
        issue_book()
    elif c == 2:
        print("Returning Book")
        return_book()
    elif c == 3:
        print("Adding  Student")
        add_student()
    elif c == 4:
        print("Adding Book")
        add_book()
    elif c == 5:
        print("Detail of all the books in the Library")
        book_details()
    elif c == 6:
        print("Detail of all the Students")
        student_details()
    elif c == 7:
        print("All Information")
        statistics()
    elif c == 8:
        exit()
    else:
        print("Sorry User\nInvalid Input")
    ans = input("Want to rerun the program ? ( Y / N )")
