#account number, password
#init to ask for registration/login

from accountNumGen import generateAccountNo
from operations import bankOperations

database = {}

def init():
    print('Welcome to BankPHP')
    choice = int(input('What do you want to do? \n 1. Login \n 2. Create an account \n 3. Exit app \n'))
    if(choice==1):
        print('Log into your account')
        login()
    elif(choice==2):
        regChoice = int(input('Do you want to create an account? 1 (Yes), 2 (No) \n'))
        if(regChoice==1):
            registr()
        elif(regChoice==2):
            print('Thank you for visiting Bank PHP')
            init()
        else:
            print('Invalid selection')
            init() 
    elif(choice==3):
        exit()
    else:
        init()
        


def registr():
    print('*******CREATE ACCOUNT*******')
    email = input('What is your email address?\n')
    first_name= input('What is your First Name?\n')
    last_name= input('What is your Last Name?\n')
    password = input('Please choose a password\n')
    accountNumber = generateAccountNo()
    database[accountNumber] = [first_name, last_name, email, password]
    print('Your account has been created')
    print('** **** ***** **** ***')
    print('Your account number is %s' %accountNumber)
    print('Make sure to keep it safe. Do not show your password to anyone.')
    login()




def login():
    loginBool = int(input('Do you want to log into your account? 1. Yes. 2. No\n'))
    if(loginBool==1):
        print('*********LOG INTO YOUR ACCOUNT **********')
        userAccountNumber= int(input('What is your account number?\n'))
        userPassword = input('What is your password?\n')

        for accountNumber,userDetails in database.items():
            if(accountNumber == userAccountNumber):
                if(userDetails[3]==userPassword):
                    print('Login Successful')
                    balance =0
                    database[accountNumber].append(accountNumber)
                    database[accountNumber].append(balance)
                    bankOperations(database[accountNumber])
                    init()
                else:
                    print('Invalid account number or password')
                    login()
    elif(loginBool==2):
        print('Thank you for visiting BankPHP')
        init()
    else:
        print('Invalid selection, please try again')
        login()

init()