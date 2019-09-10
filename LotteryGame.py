import random                                                                       # Adds 'random' functionality to the application

randomNum = str(random.randint(10, 99))                                             # Generates random number and stores to variable

userNum = str(input("Please enter a random 2 digit number: "))                      # Requests string input from user and stores as a variable

UserDigOne = False                                                                  # Assigns the variable boolean value
UserDigTwo = False                                                                  # Assigns the variable boolean value

if userNum[0] == randomNum[0] or userNum[0] == randomNum[1]:                        # Control system that tests the variable boolean against two variables
    UserDigOne = True                                                               # Changes variable boolean value
    
if userNum[1] == randomNum[0] or userNum[1] == randomNum[1]:                        # Control system that tests the variable boolean against two variables
    UserDigTwo = True                                                               # Changes variable boolean value

print ("The random lottery number is: ",randomNum)                                  

if userNum == randomNum:                                                            # Tests two variable values against each other and prints if true.
    print ("Congratulations you have an exact match, you win R10 000.00")
elif UserDigOne == True and UserDigTwo == True:                                     # Displays message if both variables are true 
    print ("Congratulations you have all digits, you win R5 000.00")
elif (UserDigOne == True) or (UserDigTwo == True):                                  # Displays message if either variable is true               
    print ("Congratulations you have one correct digit, you win R1 000.00") 
else :                                                                          
    print ("Sorry no match")
