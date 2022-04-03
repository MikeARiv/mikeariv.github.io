## Electronic Portfolio developed to showcase a few key concepts I have learned over the years.

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


### Artifact 2 

Algorithms and Data Structures:

  Development of artifact 2 was utilzied to show a further enhanced login system, developed with Java and utilziation of MD5 hash algorithm for password storage into a database.  Continued used of credentials.txt for ease of use.  This artifact was inspired by aspects of previous systems made in java and python.  

  [Artifact 2](https://github.com/MikeARiv/mikeariv.github.io/blob/main/authenticationSystem.java)
  
  Highlights:
  
     Define a function to accept user input for username and password
  
     Translate and encrypt password for storage in database
  
     Ability to call username and password to validate user from a database

```markdown
# Example code snippet of enhancements:

//Username request
   System.out.println("Please enter username: ");   //requesting username input
   username = scnr.nextLine();   //scanning for next set of words in a line in order to establish username
   if (username.equals("q")){   //if statement which allows quit if user selects q
      inputDone = true;   //allow inputDone to be true in order to end application
      System.out.println("You have now exited the session.  Goodbye");
   return;
   }
   
//Password request
   System.out.println("Please enter your password: ");   //requesting password input
   password = scnr.nextLine();   //scanning for next set of words in a line to establish password
   if (password.equals("q")){   //if statement which allows quit if user selects q
      inputDone = true;   //allow inputDone to be true in order to end application
      System.out.println("You have now exited the session.  Goodbye");   //end statement printed to user for validation of end
   return;
   }

//Translate and encrypt password
   else {
      String original = password;  //Replace "password" with the actual password inputted by the user
		  MessageDigest md = MessageDigest.getInstance("MD5");
		  md.update(original.getBytes());
		  byte[] digest = md.digest();
      StringBuffer sb = new StringBuffer();
		  for (byte b : digest) {
			   sb.append(String.format("%02x", b & 0xff));
		     }
//Reading in credentials from database
     URL path = authenticationSystem.class.getResource("credentials.txt");   //setting URL path to the same folder in which our document is located
		 File f = new File(path.getFile());   //input for filepath to be read in
		 BufferedReader reader = new BufferedReader(new FileReader(f));   //buffer stated to read and store input from File f
		 line = null;
```

### Artifact 3 

Databases:

  Artifact created to showcase Create, Read, Update and Delete functionality utilizing a python script.

  [Artifact 3](https://github.com/MikeARiv/mikeariv.github.io/blob/main/MongoDB_CRUD.py)
  
  Highlights:
  
     Query functionality, and ability to find records
  
     Ability to Create, Read, Update and Delete Records


```markdown
# Example code snippet of enhancements:
//Create user accounts in MongoDB.
    def create(self, data):
        if data is not None:
            self.database."replace with your databse name".insert(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")

//Ability to read a query in MongoDB for finding one of a data type you are looking for.
    def read(self,data):
        if data is not None:
            return self.database."replace with your databse name".find_one(data)
        else:
            print('Nothing to read, because data parameter is empty')
        return False
        
//Update method for updating a record in your MongoDB
  def update(self, find=dict(), replace=dict()): #utilized to find and replace items
    if find is not None: #if function performing find and replace
        toUpdate = self.database."replace with your databse name".update_many(find, {"$set":replace})
        return json.dumps(str(toUpdate.modified_count) + ' record has been updated')
    else:
        raise Exception("Did not work")
          
//Delete method to delete a record
  def delete(self, data=dict()):
    if data is not None:
        return json.dumps(self.database."replace with your databse name".remove(data))
    else:
        raise Exception("Did not work")
```
