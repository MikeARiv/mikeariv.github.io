'''
This is a generic user login system.
Please adjust to the needs.
Headers and comments provided for ease of use.
'''

#function used to pass in username and password, for validation and input of both from credentials.txt
'''
Utilize this section to adapt to your needs, as in change db to pass in SSH or MongoDB information for logon if necessary.
credentials.txt was used as a temporary solution and should be address based on your needs, and can be a different file altogether.
'''
def registration():
    db = open("credentials.txt" , "r") #For ease of access, we are using a text file as database and the r option for read
    username = input("Create username:") #pass in username for registration
    password = input("Create password:") #pass in password for registration
    password1 = input("Please confirm your password:") #validation of password
    d = [] #store username
    f = [] #store password

    for i in db:
        a,b = i.split(", ") #remove comma and space so password stands alone if we print it out
        b = b.strip()
        d.append(a) #ability to append username
        f.append(b) #ability to append password
    data = dict(zip(d, f))
    
    if password !=  password1: #validation of created password
        print("Password validation did not succeed, please confirm your password")
        registration()
    else:
        if len(password) <= 5: #set limit of 5 for password length.  Adjust to your password requirements, Length of 15 recommended
            print("Password is too short, please utilize a minimum of 5 characters") #update as required for character length change
            registration()
        elif username in db: #check to see if username exist
            print("Username exist")
            registration()
        else: #allow append of username and password
            db = open("credentials.txt" , "a")
            db.write(username+", "+password+ "\n")
            print("***User Creation Was Successful***")

#function used to validate username and password from credentials.txt
'''
Change to your database for credential verification or create a document that is secure to abstract and validate users from.
'''
def access():
    db = open("credentials.txt" , "r")
    username = input("Enter username:")
    password = input("Enter password:")

    if not len(username or password) <= 1:
        d = [] #store username
        f = [] #store password

        for i in db:
            a,b = i.split(", ") #remove comma and space so password stands alone
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]: #checks if username is in the database
                try:
                    if password == data[username]: #checks if the password and the username matches
                        print("Login Successful")
                        print("Good morning," , username , "\nWelcome to the dashboard for our Employee Tracker")
                    else:
                        print("Invalid Username or Password")
                except:
                    print("Incorrect Username or Password")
            else:
                print("Username or password does not exist")
        except:
            print("Username or password does not exist")
    else:
        print("Please enter a value")
        
#function to develop a home dashboard
'''
Creates an option dashboard for user selection and functionality
Add additional options if necessary via an added else if statement.
'''
def dashboard(option = None):
    option = input("**********Authorized personnel only********\nFor Login enter 1:\nFor New User enter 2:\nTo Quit, Enter 3:\n**********Authorized personnel only********\n")
    if option == "1":
        access()
    elif option == "2":
        registration()
    elif option == "3":
        print("Exiting System . . .")
        SystemExit()
    else:
        print("Please select an option")

dashboard()
