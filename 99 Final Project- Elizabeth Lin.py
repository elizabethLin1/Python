#Elizabth Lin
#99 Final Project
#January 10, 2018

#defining my functions----------------------------------------------------------
def display_menu():#creating first function, set the name of it
                   #used to beginning the program
    choice=input("        Welcome to First Bank of Dad\n"+

          "              1)Request a withdrawal\n"+
          "              2)Make a deposit\n"+
          "              3)Check balance\n"+
          "              0)Exit the program\n\n"+

          "              Enter your choice>")
                                         #intro the program, get the choice from the user
    return choice                        #gives this value back into the main program

def withdrawal(bal):                     #creating second function, defined the name
    money=int(input("Enter the money>")) #get the value from user
    if (money>bal):                      #check if the withdrawal money <=balance
        print("Sorry, It is more than your balance.\n Please enter the valid number.")
    else:
        bal=bal-money                    #get new balance number after withdrawal
    return bal                           #give this value back into the main program

def  deposit(ball):                      #creating third funtion, defined the name
    money=int(input("Enter the money>")) #get the value from user
    ball=ball+ money                     #get the new balance after deposit
    return ball                          #gives this value back into the main program
    
    


# main program---------------------------------------------------------------
import random#get random number
balance=random.randint(100.00,5000.00)    #get random balance, it has limitation
response="999"                              #saved a variable
while (response!="0"):                      #use while loop to run the function(print the menu) over and over again
    response=display_menu()               #running the first beginning function
    if response == "1":                   #use if-elif-else to check the choice then run the match function
        balance=withdrawal(balance)
        print("This is your balance now:",balance)

    elif response == "2":
        balance=deposit(balance)
        print("This is your balance now:",balance)

    elif response == "3":
        print("This is your balance:",balance)

    elif response=="0":
        print("Thanks. Looking forward to using next time!!!")
               
    else:
        print("Please enter valid choice.")




    
