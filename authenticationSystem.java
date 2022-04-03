import java.util.*;
import java.io.*;
import java.net.URL;
import java.security.*;

public class authenticationSystem {
   public static void main(String[] args) throws IOException , NoSuchAlgorithmException {
      Scanner scnr = new Scanner(System.in);   //Input stream for standard input
      String username = "";   //Username
      String password = "";   //Password
      boolean inputDone = false;   //Flag to indicate next iteration
      int totalAttempts = 3;   //int for how many times while will loop as long as true
      String line = "";   //variable set for line while reading lines later in the script

      //While loop until user enters q to quit:
      while ((!inputDone) || (totalAttempts != 0)) {   //while loop

         //Message of the day:
         System.out.println("\n     **********Authorized personnel only********    \n\n Select 'q' to quit.  \n\n Welcome to the Zoo's verification system.  \n\n For further assistance, please contact the admin section at 555-5555. \n\n     **********Authorized personnel only********     \n");


         //Username and password request
         System.out.println("Please enter username: ");   //requesting username input
         username = scnr.nextLine();   //scanning for next set of words in a line in order to establish username
         if (username.equals("q")){   //if statement which allows quit if user selects q
            inputDone = true;   //allow inputDone to be true in order to end application
            System.out.println("You have now exited the session.  Goodbye");
         return;
         }

         System.out.println("Please enter your password: ");   //requesting password input
         password = scnr.nextLine();   //scanning for next set of words in a line to establish password
         if (password.equals("q")){   //if statement which allows quit if user selects q
            inputDone = true;   //allow inputDone to be true in order to end application
            System.out.println("You have now exited the session.  Goodbye");   //end statement printed to user for validation of end
         return;
         }
         else {
     		String original = password;  //Replace "password" with the actual password inputted by the user
		    MessageDigest md = MessageDigest.getInstance("MD5");
		    md.update(original.getBytes());
		    byte[] digest = md.digest();
         StringBuffer sb = new StringBuffer();
		    for (byte b : digest) {
			sb.append(String.format("%02x", b & 0xff));
		    }
           System.out.println("original:" + original);  //used to show string comparison
		   System.out.println("digested:" + sb.toString()); //used to show string comparison in testing

         //Reading in credentials file
         URL path = authenticationSystem.class.getResource("credentials.txt");   //setting URL path to the same folder in which our document is located
		 File f = new File(path.getFile());   //input for filepath to be read in
		 BufferedReader reader = new BufferedReader(new FileReader(f));   //buffer stated to read and store input from File f
		 line = null;


            //Validation of credentials, While loop:
			while ((line = reader.readLine()) != null) {
                //For admin validation:
				if (line.contains(username) && line.contains(password) && line.contains("admin")) {   //validation of username, password only pertaining to admin accounts
                   path = authenticationSystem.class.getResource("admin.txt");   //setting URL path to the same folder in which our document is located
			       f = new File(path.getFile());   //input for filepath to be read in
			       reader = new BufferedReader(new FileReader(f));   //buffer stated to read and store input from File f
			       line = null;
			       while ((line = reader.readLine()) != null) {
				      if (line.length() > 0) {
					     System.out.println(line);   //print statement accessing admin.txt and printing information contained in the file
                      }
                   }
                 return;
                 }


                 //For zookeeper validation:
                 if (line.contains(username) && line.contains(password) && line.contains("zookeeper")) {   //validation of username, password only pertaining to zookeeper accounts
                   path = authenticationSystem.class.getResource("zookeeper.txt");   //setting URL path to the same folder in which our document is located
			       f = new File(path.getFile());   //input for filepath to be read in
			       reader = new BufferedReader(new FileReader(f));   //buffer stated to read and store input from File f
			       line = null;
			       while ((line = reader.readLine()) != null) {
				      if (line.length() > 0) {
					     System.out.println(line);   //print statement accessing zookeeper.txt and printing information contained in the file
                      }
                   }
                 return;
                 }


                 //For veterinarian validation:
                 if (line.contains(username) && line.contains(password) && line.contains("veterinarian")) {   //validation of username, password only pertaining to veterinarian accounts
                   path = authenticationSystem.class.getResource("veterinarian.txt");   //setting URL path to the same folder in which our document is located
			       f = new File(path.getFile());   //input for filepath to be read in
			       reader = new BufferedReader(new FileReader(f));   //buffer stated to read and store input from File f
			       line = null;
			       while ((line = reader.readLine()) != null) {
				      if (line.length() > 0) {
					     System.out.println(line);   //print statement accessing veterinarian.txt and printing information contained in the file
                      }
                   }
                 return;
                 }
              }
              reader.close();    //closes out open file
              System.out.println("Incorrect Username or Password.");
              totalAttempts--;   //sets total count for attempts
              System.out.println("\n     ******** " + totalAttempts + " more attempts left to login" + "********     \n");
              reader.close();   //closes out open file
           }                  
         //If statement exiting after a Maximum of 3 attempts of incorrect username and password
         if (totalAttempts == 0) {
            System.out.println("Maximum number of attempts exceeded");
         return;
         }
         }
   return;                
   }  
}




