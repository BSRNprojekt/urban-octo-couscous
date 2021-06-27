 import datetime
import random
import string

import mysql.connector
import pyperclip
import stdiomask
from prettytable import PrettyTable

tab = PrettyTable()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql123$",
    database="passwords"
)
check_in_mas = 1
while check_in_mas == 1:

    master1 = stdiomask.getpass('make a new master pass :', '*')
    master2 = stdiomask.getpass('Enter again  :', '*')

    if master1 == master2:
        print("Master pass successfully created ")
        master3 = master2
        master2 = master1

        in_menu = 0
        while in_menu == 0:

            in_pass = stdiomask.getpass('Enter a master pass to go to menu: ', '*')

            if in_pass == master3:
                print("Welcome")

                option = 9
                while option > 8 or option < 1:

                    date_now = datetime.datetime.now()
                    minutes = 10
                    date_change = datetime.timedelta(minutes=minutes)
                    date_after = date_now + date_change
                    print("Start time: ", date_now)
                    print("End time  : ", date_after)

                    print("What you would like to do today ? \n"
                          "-------------------------------------\n"
                          "-------------------------------------\n"
                          "| 1 | Add a new Activity. \n"
                          "-------------------------------------\n"
                          "| 2 | Change a Activity . \n"
                          "-------------------------------------\n"
                          "| 3 | Delete Activity by Website. \n"
                          "-------------------------------------\n"
                          "| 4 | Search Activity by Website.\n"
                          "-------------------------------------\n"
                          "| 5 | Search Activity by Title.\n"
                          "-------------------------------------\n"
                          "| 6 | Show all current Activity\n"
                          "-------------------------------------\n"
                          "| 7 | Change Masterpassword. \n"
                          "-------------------------------------\n"
                          "| 8 | Quit."
                          "\n-------------------------------------"
                          "\n-------------------------------------")
                    option = int(input("-->>Enter option: "))

                    if datetime.datetime.now() > date_after:
                        print("time over")
                        in_menu = 0
                        break

                    if option == 1:
                        tab1 = PrettyTable()


                        class titel:
                            def __init__(self, titel, website, username, password):
                                self.titel = titel
                                self.website = website
                                self.username = username
                                self.password = password


                        again = "yes"
                        count = 0
                        tableList = []

                        while again == "yes":
                            if datetime.datetime.now() > date_after:
                                print("time over")
                                in_menu = 0
                                break

                            title = input("-->>Enter a Title: \n")
                            website = input("-->>Enter a website: \n")
                            user = input("-->>Enter a username: \n")
                            print("\n***For Password***\n")
                            print("1-->> Manual: \n")
                            print("2-->> Auto-generate: \n")

                            pass_op = int(input("-->>Enter Option: \n"))

                            if (pass_op == 1):
                                password = stdiomask.getpass('-->>Enter your password: \n', '*')
                                print("\n-->>Your Password: ", password, "\n")

                            elif (pass_op == 2):

                                length = int(input("-->>Enter a length: \n"))

                                while (length < 8 or length > 12):
                                    print("\n***Invalid lenght***\n")
                                    length = int(input("-->>Enter a length(8-12): \n"))

                                password_characters = string.ascii_letters + string.digits + string.punctuation
                                password = ''.join(random.choice(password_characters) for i in range(length))
                                print("-->>Random password :", password, "\n")

                            tableList.append(titel(title, website, user, password))

                            tab1.field_names = ["Title", "Website", "Username", "Passwords"]
                            tab1.add_row([title, website, user, password])
                            print(tab1)

                            mycursor = mydb.cursor()

                            sql = "INSERT INTO activity (title, website, username, password) VALUES (%s, %s,%s,%s)"
                            val = (title, website, user, password)
                            mycursor.execute(sql, val)

                            mydb.commit()
                            count = count + 1

                            print(count, "record inserted.")

                            again1 = input("enter 'yes' for again or enter any key to  stop\n"
                                           "-->>  ")
                            if again1 == ("yes"):
                                again = again1
                            else:
                                again = ""
                                print(count, "record inserted.")
                                print(input("enter any key to go to main Menu"))
                                option = 9


                    elif option == 2:
                        ag2 = "yes"
                        while ag2 == "yes":
                            if datetime.datetime.now() > date_after:
                                print("time over")
                                in_menu = 0
                                break

                            mycursor = mydb.cursor()

                            sql = "UPDATE activity SET website = %s WHERE website = %s"
                            wb = (input("enter a new website: "), input("enter a old website: "))
                            mycursor.execute(sql, wb)

                            sql = "UPDATE activity SET title = %s WHERE title = %s"
                            tl = (input("enter a new title: "), input("enter a old title: "))
                            mycursor.execute(sql, tl)

                            sql = "UPDATE activity SET username = %s WHERE username = %s"
                            un = (input("enter a new username: "), input("enter a old username: "))
                            mycursor.execute(sql, un)

                            sql = "UPDATE activity SET password = %s WHERE password = %s"
                            ps = (input("enter a new password: "), input("enter a old password: "))
                            mycursor.execute(sql, ps)

                            mydb.commit()

                            in2 = input("Enter 'yes' to again else 'any key' to go to main menu.")
                            if in2 == "yes":
                                ag2 = in2
                            else:
                                ag2 = ""
                                option = 9

                    elif option == 3:
                        ag3 = "yes"
                        while ag3 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("time over")
                                in_menu = 0
                                break

                            mycursor = mydb.cursor()

                            sql = "DELETE FROM activity WHERE website = %s"
                            del_wb = (input("Enter a website to delete: "),)
                            mycursor.execute(sql, del_wb)
                            mydb.commit()

                            in3 = input("Enter 'yes' to again else 'Any key' to go to main Menu. ")
                            if in3 == "yes":
                                ag3 = in3
                            else:
                                ag3 = ""
                                option = 9

                    elif option == 4:
                        ag4 = "yes"
                        while ag4 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("time over")
                                in_menu = 0
                                break

                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM activity WHERE website = %s "
                            wb = (input("enter a website: "),)

                            mycursor.execute(sql, wb)

                            myresult = mycursor.fetchall()

                            for x in myresult:
                                print("Password is copied to clipboard!!!")
                                pyperclip.copy(x[4])



                            in4 = input("Enter 'yes' to again, else any key to go to main Menu.")
                            if in4 == "yes":
                                ag4 = in4
                            else:
                                ag4 = ""
                                option = 9

                    elif option == 5:
                        ag5 = "yes"
                        while ag5 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("time over")
                                in_menu = 0
                                break

                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM activity WHERE title = %s "
                            tl = (input("enter a title : "),)

                            mycursor.execute(sql, tl)

                            myresult = mycursor.fetchall()

                            for x in myresult:
                                print("Password is copied to clipboard!!!")
                                pyperclip.copy(x[4])

                            in5 = input("Enter 'yes' to again, else any key to go to main Menu.")
                            if in5 == "yes":
                                ag5 = in5
                            else:
                                ag5 = ""
                                option = 9

                    elif option == 6:
                        mycursor = mydb.cursor()

                        mycursor.execute("SELECT * FROM activity")

                        myresult = mycursor.fetchall()
                        tab.field_names = ["ID", "Title", "Website", "Username", "Passwords"]

                        for x in myresult:
                            tab.add_row(x)
                        print(tab.get_string(title="Activities"))

                        if mycursor.rowcount == 0:
                            print("there are no records")
                        else:
                            print("there are ", mycursor.rowcount, " records")

                        op6 = input("enter any key to go to main menu: ")

                        if op6 == "":
                            option = 9
                        else:
                            option = 9


                    elif option == 7:

                        a = 0
                        while a == 0:
                            ask7 = stdiomask.getpass('Enter a current master pass :', '*')
                            print(ask7)

                            if ask7 != in_pass:
                                a = 0


                            else:
                                a =""
                                b = 0
                                while b == 0:
                                    mas_chg1 = stdiomask.getpass('Enter a new master pass :', '*')
                                    mas_chg2 = stdiomask.getpass('Enter a new master pass again :','*')

                                    if mas_chg1 != mas_chg2:
                                        b = 0

                                    else:
                                        b = ""
                                        print("Masterpass changed sucessfully !!")
                                        master3 = mas_chg2
                                        in_pass = master3
                                        in_menu = 0



                    elif option == 8:
                        in_menu = 0


                    else:
                        if datetime.datetime.now() > date_after:
                            print("time over")
                            in_menu = 0
                            break

                        option = 9

            else:
                print("Enter a correct master pass")
                in_menu = 0
    else:
        print("Pass didn't match")
        check_in_mas = 1
