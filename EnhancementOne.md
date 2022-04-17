## Enhancement One: Software Engineering & Design

The artifact chosen for was part of a final project for CS 340 and was created in October of 2021. Its purpose was to provide access to a dabase via username and password.  Upon further development, I found limitations in its use and have updated the artifact to show additional functionality.

For Employee_Tracker.py, I wanted to showcase my ability to create a basic login feature, with validation of username and password from a database.  Additionally, I wanted to be able to build upon this concept for the next few artifacts to include encryption of passwords to be stored and, once a person securely logs in, to display data from a database on a front-end system.

The improvement of this artifact came from creation of a login system that was separate from the database login.  This helps to showcase my knowledge on development of login systems with python, vice utilization of MongoDB.  With MongoDB, to show utilization of a database to another user that may be trying to understand this system, having a localhost and port that is not relative to their system could inhibit functionality on their end. (line 17 of animal_shelter.py).  For this reason, I created a new python script, to implement a text file that you could utilize and access as long as it is dropped in the same folder as the Employee_Tracker.py.

The creation of the access function was used to add validation of credentials once a user logs into the system or it will give errors based on duplicates in the file or if there is not account of that name.  Additional dashboard functionality was created as well, to give a user the option to create a new user, login with existing user, or quit the system.

I do believe the course objective was met, but not to the ability I am striving to get.  I say this because I plan to further enhance this login system to be encrypted and to have the ability to log into a database to display information from the queries onto a front-end system.  A few more updates as well to add update and delete functionality once the database is established. We can also add functionality in the form of deleting unwanted user accounts but pending more work with encryption to ensure we can delete all data once we have encryption added.

I was reintroduced to nesting of if and else statements and found them easier to work with compared to the while statement.  This module this require me to review much of the concepts I learned in java and reworking them to be on python.  I had to be reminded of how to read and pass in information from files with python, as well as changing syntax.  Overall, I enjoyed this module and looking forward to adding encryption and database functionality in the next few weeks. 

[Original Artifact ](https://mikeariv.github.io/animal_shelter.py)
**Link to Enhancement**
[Enhancement One ](https://mikeariv.github.io/Employee_Tracker.py)

**Porfolio Links**<br>
* [Professional Self-Assessment](https://mikeariv.github.io/index.html)<br>
* [Refinement Plan & Code Review](https://mikeariv.github.io/CodeReview.html)<br>
* [Enhancement One](https://mikeariv.github.io/EnhancementOne.html)<br>
* [Enhancement Two](https://mikeariv.github.io/EnhancementTwo.html)<br>
* [Enhancement Three](https://mikeariv.github.io/EnhancementThree.html)
