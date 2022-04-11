### Artifact 1 

Software Design / Enginnering:

  Initial development for a Python Login system pulling credentials from a database.  For ease of use, a .txt file was used.  Update as needed to check functionality on your file system.

  [Artifact 1](https://github.com/MikeARiv/mikeariv.github.io/blob/main/Employee_Tracker.py)
  
  Highlights:
  
     Username and Password acceptance.
  
     Read elements from a database.
  
     Update and append user accounts to said database.

```markdown
# Example code snippet of enhancements:
//Function to show utilization of database in the form of a text file for username/password placement:
def registration():
    db = open("credentials.txt" , "r") #For ease of access, we are using a text file as database and the r option for read
    username = input("Create username:") #pass in username for registration
    password = input("Create password:") #pass in password for registration
    password1 = input("Please confirm your password:") #validation of password
    d = [] #store username
    f = [] #store password

//Ability to append username and passwords:
    for i in db:
        a,b = i.split(", ") #remove comma and space so password stands alone if we print it out
        b = b.strip()
        d.append(a) #ability to append username
        f.append(b) #ability to append password
    data = dict(zip(d, f))

//Validation of username and password from database:
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
```
