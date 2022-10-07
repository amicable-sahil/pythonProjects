import datetime
from pickle import TRUE
import psycopg2

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



# Connection with postgres database 
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'admin'
port_id = 5432


connection = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)
cur = connection.cursor()




#  inserting data of users who wants to register------------------------
def insert_data(uName, pWord):

    insert_user_tb = 'INSERT INTO users VALUES (%s, %s)'
    insert_data = (uName, pWord)

    cur.execute(insert_user_tb, insert_data)




#  creating a user table to store registered users----------------------------

create_tb = ''' CREATE TABLE IF NOT EXISTS users (
                        username   text PRIMARY KEY,
                        password   text NOT NULL ) '''
                    
cur.execute(create_tb)




# creating contacts table to store all the contacts init---------------------------
create_contact_tb = ''' CREATE TABLE IF NOT EXISTS contact_book (
                        con_id          int PRIMARY KEY,
                        con_firstname   text NOT NULL,
                        con_lastname    text NOT NULL,
                        con_email       text, 
                        con_number      int ) '''

cur.execute(create_contact_tb)




#  This function allows user to add contact details------------------------------- 
def add_contacts(c_id, c_fname, c_lname, c_email, c_num):
    insert_contacts = 'INSERT INTO contact_book VALUES (%s, %s, %s, %s, %s)'
    contacts_data = (c_id, c_fname, c_lname, c_email, c_num)

    cur.execute(insert_contacts, contacts_data)




#  This function allows user to show all contact details----------------------------- 
def show_all_contacts():
    show_contacts = 'SELECT * FROM contact_book'
    cur.execute(show_contacts)

    print("--------------------------------------------------------------------------------------")
    print(f"|  {bcolors.OKCYAN}Contact Id{bcolors.ENDC}   |  {bcolors.OKCYAN}First Name{bcolors.ENDC}   |  {bcolors.OKCYAN}Last Name{bcolors.ENDC}   |  {bcolors.OKCYAN}Email{bcolors.ENDC}             |  {bcolors.OKCYAN}NUmber{bcolors.ENDC}        |")
    
    for record in cur.fetchall():
        print("| ",record[0], " "*(11-len(str(record[0]))), "| ",record[1], " "*(11-len(str(record[1]))), "| ",record[2], " "*(10-len(record[2])), "|",record[3], " "*(17-len(record[3])), "|",record[4], " "*(13-len(str(record[4]))), "|")
    
    print("--------------------------------------------------------------------------------------")





#  This function allows user to show a specific contact detail------------------------- 
def show_specific_contact(c_name):
    show_contacts = 'SELECT * FROM contact_book'
    cur.execute(show_contacts)


    print("--------------------------------------------------------------------------------------")
    print(f"|  {bcolors.OKCYAN}Contact Id{bcolors.ENDC}   |  {bcolors.OKCYAN}First Name{bcolors.ENDC}   |  {bcolors.OKCYAN}Last Name{bcolors.ENDC}   |  {bcolors.OKCYAN}Email{bcolors.ENDC}             |  {bcolors.OKCYAN}NUmber{bcolors.ENDC}        |")
    
    for record in cur.fetchall():
        if record[1] == c_name:
            print("| ",record[0], " "*(11-len(str(record[0]))), "| ",record[1], " "*(11-len(str(record[1]))), "| ",record[2], " "*(10-len(record[2])), "|",record[3], " "*(17-len(record[3])), "|",record[4], " "*(13-len(str(record[4]))), "|")
            break
    else:
        print("Contact not found")
    
    print("--------------------------------------------------------------------------------------")




#  This function allows user to delete a specific contact-------------------------

def del_contact(c_name):
    cur.execute("DELETE FROM contact_book WHERE con_firstname = '{}'".format(c_name))
 



#  This function allows user to update a specific contact---------------------------

def update_contact(new_firstname, new_lastname, new_email, new_number, old_firstname):

    update_con = "UPDATE contact_book SET con_firstname = '{}', con_lastname = '{}', con_email = '{}', con_number = {} WHERE con_firstname = '{}' ".format(new_firstname, new_lastname, new_email, new_number, old_firstname) 

    cur.execute(update_con)


    



#  Verifing if user name is already exists------------------------------
def verify_username_for_registration(name):
    cur.execute('SELECT * FROM users')
    for record in cur.fetchall():
        if record[0] == name:
            print(f"{bcolors.WARNING}Warning: Username already exists, choose something else!{bcolors.ENDC}")
            exit()
        




#  Check contact exists or not-------------------------------------------
def check_contact(name):
    cur.execute('SELECT * FROM contact_book')
    for record in cur.fetchall():
        if record[1] == name:
            return True





#  Verifing that user is registered or not-------------------------------------------
def verify_username_for_login(uName):
    cur.execute('SELECT * FROM users')

    for record in cur.fetchall():
        if uName == record[0]:
            pWord = input("Password: ")
            if record[1] == pWord:
                print(f"{bcolors.OKGREEN}[You are logged in]{bcolors.ENDC}")
                print(day, month, year, sep="-", end="  ")
                print(tm)
                print("------------------------------")
                break
            else:
                print(f"{bcolors.WARNING}Please enter correct password{bcolors.ENDC}")
                exit()
            
    else:
        print(f"{bcolors.WARNING}Username not found, Please enter correct username or sign up!{bcolors.ENDC}") 
        exit()




print()
print(f"{bcolors.OKCYAN}-> Please sign up and log in to access the phone book{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}-> If you are already registered then log in{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}-> Press 'l' for log in and press 'r' for registration{bcolors.ENDC}")
print()
verify = input(f"{bcolors.BOLD}[l/r] {bcolors.ENDC}")
print()

x = datetime.datetime.now()
day = x.strftime("%d")
month = x.strftime("%b")
year = x.strftime("%Y")
tm = x.strftime("%X")

if verify == "r":
    user_name = input("Please enter username: ")
    verify_username_for_registration(user_name)

    pass_word = input("Please enter password: ")

    insert_data(user_name, pass_word)

    print()
    print(f"{bcolors.OKGREEN}You registered successfully{bcolors.ENDC}")
    print(day, month, year, sep="-", end="  ")
    print(tm)
    print("------------------------------")


elif verify == "l":
    user_name = input("Please enter username: ")
    
    verify_username_for_login(user_name)

    print(f"{bcolors.BOLD}What do you want to do?{bcolors.ENDC}")
    print("[view -a]  to view all saved contacts")
    print("[view]     to view a specific contact")
    print("[add]      to add a contact")
    print("[del]      to delete a contact")
    print("[update]   to update an existing contact")
    print("[exit]     to exit the program")
    print()
    ans = input()

    match ans:
        case "view -a":
            print()
            show_all_contacts()

        case "view":
            print()
            show_specific_contact(input("Enter contact name you want to find "))

        case "add":
            print()

            id = input("Enter ID: ")
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            email = input("Enter Email: ")
            number = input("Enter Number: ")
            add_contacts(id, fname, lname, email, number)

            print(f"{bcolors.OKGREEN}Contact added successfully{bcolors.ENDC}")

        case "del":
            print()
            
            name = input("Enter contact name you want to delete ")
            if check_contact(name) == True:
                del_contact(name)
            else:
                print("Contact does not exists")
            
            print(f"{bcolors.OKGREEN}Contact deleted successfully{bcolors.ENDC}")


        case "update":
            print()
            c_name = input("Enter contact name you want to update ")

            if check_contact(c_name) == True:
                n_firstname = input("Enter new first name ")
                n_lastname = input("Enter new last name ")
                n_email = input("Enter new email ")
                n_number = input("Enter new number ")
                update_contact(n_firstname, n_lastname, n_email, n_number, c_name)
                print(f"{bcolors.OKGREEN}Contact updated successfully{bcolors.ENDC}")

            else:
                print("Contact does not exists")


        case _:
            exit()



else:
    exit()



connection.commit()

cur.close()
connection.close()