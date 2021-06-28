import datetime  #Das Modul besteht aus Funktionen und Klassen zur Manipulierung von Datum und Zeit
import random    #Das benutzen wir zur Generierung von zufälligen Nummern
import string    #Zur Formatierung und Manpulierung von Strings
import mysql.connector   #Ermöglicht unser Programm auf SQL Datenbank zuzugreifen
import pyperclip      #gilt als Plattform zum Kopieren und Einfügen in Zwischenablage
import stdiomask     #setz die Eingabe in Sternchen(***) um
from prettytable import PrettyTable #Python Bibliothek zur Anzeige tabellarischer Daten

tab = PrettyTable() #Name unserer Tabelle
#Erstellung einer Verbindung mit einer Datenbank
mydb = mysql.connector.connect(
    host="localhost",   #Zugangsdaten
    user="root",
    password="Mysql123$",
    database="passwords"
)

print("     ___________________________    ")
print(" <<< WELCOME TO PASSWORD MANAGER >>> ")
print("     ---------------------------    ")
sec_info = input("\nEnter Crush Name    : ")  #persönliche Frage an den Benutzer. Die Antwort wird hier gespeichert.
check_in_mas = 1
#Erstellung ein neues Master Passwort
while check_in_mas == 1:
    master1 = stdiomask.getpass('Make New Master Pass   : ', '*')
    master2 = stdiomask.getpass('Enter Again    : ', '*')
    mp_count = 3 #Anzahl der vorhandenen Versuche
#Hier wird geprüft, ob das Passwort erfolgreich erstellt ist oder nicht
    if master1 == master2:
        print("\n   <<< Master Pass Successfully Created >>>    ")
        master3 = master2
        master2 = master1
#Angabe der Häufigkeit, mit der ndas Passwort angefordert wird
        zeit_festlegen = int(input("\nEnter Login time  : "))
        in_menu = 0
#Eingabe des Passwortes zum Zugriff auf das Passwort Manager
        while in_menu == 0:
            in_pass = stdiomask.getpass('Enter Master Pass  : ', '*')
            if in_pass == master3:
                print("\n <<< WELCOME >>> \n") # Wird auf der Konsole angezeigt,wenn das Passwort richtig ist
#Mit diesem Codeschnitt wird es sichergestellt,dass das Master Passwort angefordert wird in dem von Benutzer angegebene Frequenz.
                date_now = datetime.datetime.now() #gibt die aktuelle Zeit an
                minutes = zeit_festlegen
                date_change = datetime.timedelta(minutes=minutes) #konvertiert die Zeit in Minuten
                date_after = date_now + date_change
                print("Start time   : ", date_now)
                print("End time     : ", date_after)
                option = 9
#Hier stehen die verschiedenen Funktionalitäten unseres Passwort Managers
                while option > 8 or option < 1:
                    print("\n   <<< What You Would Like To Do Today? >>>    \n"
                          "-------------------------------------\n"
                          " | 1 |    Add  new Activity. \n"
                          "-------------------------------------\n"
                          " | 2 |    Change Activity . \n"
                          "-------------------------------------\n"
                          " | 3 |    Delete Activity By Website. \n"
                          "-------------------------------------\n"
                          " | 4 |    Search Activity By Website.\n"
                          "-------------------------------------\n"
                          " | 5 |    Search Activity By Title.\n"
                          "-------------------------------------\n"
                          " | 6 |    Show All Saved Activity\n"
                          "-------------------------------------\n"
                          " | 7 |    Change Master pass. \n"
                          "-------------------------------------\n"
                          " | 8 |    Quit."
                          "\n-------------------------------------")
#Eingabe der Auswahl
                    option = int(input("Enter Option    : "))
#Meldung zur Eingabe des Master Passwortes
                    if datetime.datetime.now() > date_after:
                        print("_____________________________________")
                        print("--------------TIME-OVER--------------")
                        print("-------------------------------------")
                        in_menu = 0
                        break
#Einträge speichern
                    if option == 1:
                        tab1 = PrettyTable()
                        class activity_list:
                            def __init__(self, titel, website, username, password):
                                self.titel = titel
                                self.website = website
                                self.username = username
                                self.password = password
                        again = "yes"
                        count = 0 #enthält die Summe der gespeicherten Einträgen
                        tableList = []
                        while again == "yes":

                            if datetime.datetime.now() > date_after:
                                print("_____________________________________")
                                print("--------------TIME-OVER--------------")
                                print("-------------------------------------")
                                in_menu = 0
                                break
#Zuweisung von Werten zu den Variablen
                            title = input("Enter Title  : \n")
                            website = input("Enter  Website : \n")
                            user = input("Enter  Username   : \n")
                            print("\n   <<< For Password >>>    \n") # Der Benutzer kann sein Passwort selbst erstellen oder vom Programm generieren lassen
                            print(" 1: For Manual : ")
                            print(" 2: For Auto Generate  : \n")
                            pass_op = int(input("Enter Option   : "))
#Erstellung des Passwortes durch den Benutzer
                            if (pass_op == 1):
                                password = stdiomask.getpass('Enter Password    : ', '*')
                                print("\n   <<< Password Saved >>>    ")
#Angabe der Stand des Passwortes
                                for x in password:
#Hat das Passwort nur Buchstaben, dann ist es schwach
                                    if password.isalpha():
                                        alpha = "   <<< Password Level : WEAK >>> "
#Hat das Passwort Buchstaben und Nummern, dann ist es normal
                                    elif password.isalnum():
                                        alpha = "   <<< Password Level : NORMAL >>> "
#Sonst ist das Passwort stark
                                    else:
                                        alpha = "   <<< Password Level : STRONG >>> "
                                print(alpha)
#Passwort vom Programm generieren lassen
                            elif (pass_op == 2):
                                length = int(input("Enter Length(8-12)  : \n")) #Länge Eingabe
#Länge Prüfung
                                while (length < 8 or length > 12):
                                    print("\n <<< Invalid Length >>>    \n")
                                    length = int(input("Enter Length(8-12)  : \n"))
#Mögliche Eigenschaften des Passwortes.Es ist durch den Benutzer gewählt
                                password_option = int(input("   <<< Option >>>    "
                                                            "\n1:   For Big/small letters + Symbol + Number   "
                                                            "\n2:   For For Big/small letters "
                                                            "\n3:   For Symbol + Number"
                                                            "\n>:   "))
#Für die erste Eigenschaften
                                if password_option == 1:
                                    password_characters = string.ascii_letters + string.digits + string.punctuation
                                    password = ''.join(random.choice(password_characters) for i in range(length))
#zweite Eigenschaften
                                elif password_option == 2:
                                    password_characters = string.ascii_letters
                                    password = ''.join(random.choice(password_characters) for i in range(length))
#Dritte Eigenschaften
                                elif password_option == 3:
                                    password_characters = string.digits + string.punctuation
                                    password = ''.join(random.choice(password_characters) for i in range(length))
#Erstellung der Tabelle
                            tableList.append(activity_list(title, website, user, password))
                            tab1.field_names = ["Title", "Website", "Username", "Password"] #Attributen
                            tab1.add_row([title, website, user, "******"])    #Tupel
                            print(tab1)

                            mycursor = mydb.cursor()    #Ermöglicht das Programm auf die Datenbank zuzugreifen
                            sql = "INSERT INTO activity (title, website, username, password) VALUES (%s, %s,%s,%s)" #SQL-Anfrage zur Anfügung von Daten
                            val = (title, website, user, password)  #Variable, deren Werte in der Tabelle gespeichert werden
                            mycursor.execute(sql, val) #Funktion zur Durchführung von SQL-Anfrage
                            mydb.commit()    #Funktion zur Validierung und Speicherung von Änderungen
                            count = count + 1 #enthält die Anzahl von Tupeln
                            print(count, "Record Inserted.")
                            again1 = input("    <<< Enter 'yes' TO Repeat & Enter Any Key To Stop >>>   "
                                           "\n>:    ")

                            if again1 == ("yes"):
                                again = again1

                            else:
                                again = ""
                                print(count, "Record Inserted.")
                                option = 9
#Änderung von Einträge
                    elif option == 2:
                        ag2 = "yes"

                        while ag2 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("_____________________________________")
                                print("--------------TIME-OVER--------------")
                                print("-------------------------------------")
                                in_menu = 0
                                break
#Mögliche Änderung auf die Daten
                            change_act = int(input("Enter option to change :\n" 
                                               "    1:  Website \n"
                                               "    2:  Title \n"
                                               "    3:  Username \n"
                                               "    4:  Password \n"
                                                   ">:  "))
# Änderung von Website
                            if change_act == 1 :
                                sql = "UPDATE activity SET website = %s WHERE website = %s"
                                wb = (input("Enter New Website    : "), input("Enter Old Website    : "))
                                mycursor.execute(sql, wb)
                                mydb.commit()
#Änderung von Titel
                            elif change_act == 2:
                                sql = "UPDATE activity SET title = %s WHERE title = %s"
                                tl = (input("Enter New Title  : "), input("Enter Old Title  : "))
                                mycursor.execute(sql, tl)
                                mydb.commit()
#Änderung von Benutzername
                            elif change_act == 3:
                                sql = "UPDATE activity SET username = %s WHERE username = %s"
                                un = (input("Enter New  Username   : "), input("Enter Old Username   : "))
                                mycursor.execute(sql, un)
                                mydb.commit()
#Änderung von Password
                            elif change_act == 4:
                                sql = "UPDATE activity SET password = %s WHERE password = %s"
                                ps = (input("Enter New password   : "), input("Enter Old password   : "))
                                mycursor.execute(sql, ps)
                                mydb.commit()

                            else:
                                option =2
                            in2 = input("    <<< Enter 'yes' TO Repeat & Enter Any Key To Stop >>>   "
                                  "\n>:    ")

                            if in2 == "yes":
                                ag2 = in2

                            else:
                                ag2 = ""
                                option = 9
#Löschen von Einträgen
                    elif option == 3:
                        ag3 = "yes"

                        while ag3 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("_____________________________________")
                                print("--------------TIME-OVER--------------")
                                print("-------------------------------------")
                                in_menu = 0
                                break
#SQL-Befehl zum Löschen von Einträgen
                            mycursor = mydb.cursor()
                            sql = "DELETE FROM activity WHERE website = %s"
                            del_wb = (input("Enter Website To Delete: "),)
                            conform = stdiomask.getpass('Confirm with Master-password   : ', '*') #Bestätigung durch Master Passwort

                            if conform == in_pass:
                                mycursor.execute(sql, del_wb)
                                mydb.commit()

                            else:
                                print(" <<< Wrong Master Pass >>>    ")
                                ag3 = "yes"
                            in3 = input("    <<< Enter 'yes' TO Repeat & Enter Any Key To Stop >>>   "
                                  "\n>:    ")

                            if in3 == "yes":
                                ag3 = in3

                            else:
                                ag3 = ""
                                option = 9
#Passwort durch Website suchen
                    elif option == 4:
                        ag4 = "yes"

                        while ag4 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("_____________________________________")
                                print("--------------TIME-OVER--------------")
                                print("-------------------------------------")
                                in_menu = 0
                                break
#SQL-Anfrage zum Suchen von Einträgen
                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM activity WHERE website = %s "
                            wb = (input("Enter Website    : "),)
                            mycursor.execute(sql, wb)
                            myresult = mycursor.fetchall()
#Passwort im Clipboard kopieren
                            for x in myresult:
                                print(" <<< Password Copied To Clipboard >>>    ")
                                pyperclip.copy(x[4])
                            in4 = input("    <<< Enter 'yes' TO Repeat & Enter Any Key To Stop >>>   "
                                  "\n>:    ")

                            if in4 == "yes":
                                ag4 = in4

                            else:
                                ag4 = ""
                                option = 9
#Passwort durch Titel suchen
                    elif option == 5:
                        ag5 = "yes"

                        while ag5 == "yes":

                            if datetime.datetime.now() > date_after:
                                print("_____________________________________")
                                print("--------------TIME-OVER--------------")
                                print("-------------------------------------")
                                in_menu = 0
                                break
#SQL-Anfrage zum Suchen von Einträge durch das Titel
                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM activity WHERE title = %s "
                            tl = (input("Enter  Title   : "),)
                            mycursor.execute(sql, tl)
                            myresult = mycursor.fetchall()
#Kopieren vom Passwort im Clipboard
                            for x in myresult:
                                print(" <<< Password Copied To Clipboard >>>    ")
                                pyperclip.copy(x[4])
                            in5 = input("    <<< Enter 'yes' TO Repeat & Enter Any Key To Stop >>>   "
                                  "\n>:    ")

                            if in5 == "yes":
                                ag5 = in5

                            else:
                                ag5 = ""
                                option = 9
#Überblick von allen Daten
                    elif option == 6:

                        if datetime.datetime.now() > date_after:
                            print("_____________________________________")
                            print("--------------TIME-OVER--------------")
                            print("-------------------------------------")
                            in_menu = 0
                            break
#SQL-Anfrage zum Anzeigen von Daten
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT * FROM activity")
                        myresult = mycursor.fetchall()
                        tab.field_names = ["ID", "Title", "Website", "Username", "Password"]
#Titel der Tabelle
                        for x in myresult:
                            tab.add_row(x)
                        print(tab.get_string(title="    <<< Activities >>>  "))
#Dieser Codeschnitt ermöglicht das Programm Wiederholungen von der Tabelle zu vermeiden, falls eine Änderung gemacht wurde
                        for x in myresult:
                            tab.clear_rows()
#Prüfung der Anzahl von Einträgen in der Tabelle
                        if mycursor.rowcount == 0:
                            print(" <<< There Are No Records >>>    ")

                        else:
                            print(" <<< There Are ", mycursor.rowcount, " Records >>>   ")
                        op6 = input("    <<< Enter 'yes' TO Repeat & Enter Any Key To Stop >>>   "
                                  "\n>:    ")

                        if op6 == "":
                            option = 9

                        else:
                            option = 9
#Änderung von Master-Passwort
                    elif option == 7:
                        a = 0
#Eingabe von aktuellen Master Passwort
                        while a == 0:
                            ask7 = stdiomask.getpass('Enter Current Master Pass   :', '*')

                            if ask7 != in_pass:
                                a = 0

                            else:
                                a =""
                                b = 0
#Eingabe von neuen Master Passwwort
                                while b == 0:
                                    mas_chg1 = stdiomask.getpass('Enter New Master Pass : ', '*')
                                    mas_chg2 = stdiomask.getpass('Enter New Master Pass Again : ','*')
#Prüfung der Gleichheit der Eingaben
                                    if mas_chg1 != mas_chg2:
                                        b = 0

                                    else:
                                        b = ""
                                        print(" <<< Masterpass Changed Sucessfully >>>   ")
                                        master3 = mas_chg2
                                        in_pass = master3
                                        in_menu = 0
#Zum Beenden des Programms. Der Benutzer sollte seine Zugangsdaten eingeben, um wieder auf der Passwort Manager zuzugreifen
                    elif option == 8:
                        in_menu = 0

                    else:

                        if datetime.datetime.now() > date_after:
                            print("_____________________________________")
                            print("--------------TIME-OVER--------------")
                            print("-------------------------------------")
                            in_menu = 0
                            break
                        option = 9
#Prüfung der verbleibenden Anzahl von Versuche bei Master Passwort Eingabe
            else:
                mp_count = mp_count - 1

                if mp_count > 0:
                    print(" <<< ", mp_count, " Tries Left >>>  ")
                    in_menu = 0

                else:
                    print(" <<< No More Tries Left >>>   ")
                    sec_info_input = 11
#Bei Erschöpfung von Versuchen. Die geheime Frage beantworten
                    while sec_info_input == 11:
                        sec_info_check = input("Enter First Crush Name : ")
#Prüfung der Gleichheit von Antworten
                        if sec_info_check != sec_info:
                            sec_info_input = 11

                        else:
                            sec_info_check = ""
                            in_menu = ""
                            check_in_mas = 1
                            break

    else:
        print(" <<< Not Matched >>> ")
        check_in_mas = 1
