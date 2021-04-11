import datetime



def bankOperations(user):
    now= datetime.datetime.now()
    print('Welcome %s %s!' % (user[1], user[0]))
    print('The time is %s. Today is %s' % (now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d")))
    
    print(" ")
    accountMenu(user)

def accountMenu(user):
    print('Account Number: %s     Account Balance: $%d' % (user[4],user[5]))
    print('************ MENU ************')
    print(' 1. Check account balance \n 2. Deposit funds \n 3. Withdraw funds \n 4. Change password \n 5. Make a complaint \n 6. Logout')
    selectedOption = int(input('Select an option and press enter \n'))
    if(selectedOption==1):
        checkBalance(user)
    elif(selectedOption==2):
        fundsDeposit(user)
    elif(selectedOption==3):
        fundsWithdrawal(user)
    elif(selectedOption==4):
        passChange(user)
    elif(selectedOption==5):
        makeComplaint(user)
    elif(selectedOption==6):
        logout(user)
    else:
        print('Invalid option, try again')
        accountMenu(user)

def interlude(user):
    interludeBool = int(input('Do you want to perform another operation? 1. Yes 2. No \n'))
    if (interludeBool == 1):
        accountMenu(user)
    elif(interludeBool ==2):
        logout(user)
    else:
        print('Please select a valid option')
        interlude(user)

def checkBalance(user):
    print('*************************************************')
    print('Your current balance is $%s' % user[5])
    print('*************************************************')
    interlude(user)

def fundsDeposit(user):
    deposit= int(input('How much do you want to deposit? \n'))
    user[5]= user[5] + deposit
    print('*************************************************')
    print('You have deposited $%d, your new balance is $%d' % (deposit,user[5]))
    print('*************************************************')
    interlude(user)

def fundsWithdrawal(user):
    withdrawal = deposit= int(input('How much do you want to withdraw? \n'))
    if(withdrawal>user[5]):
        print('Insufficient balance')
    elif(withdrawal<= user[5]):
        user[5]= user[5]-withdrawal
        print('*************************************************')
        print('You have withdrawn $%d' % withdrawal)
        print('Your remaining balance is $%d'% user[5])
        print('*************************************************')
    interlude(user)

def passChange(user):
    newPass = input('Please enter a new password \n')
    newPass2 = input('Confirm your new password \n')
    if (newPass==newPass2):
        user[3] = newPass
        print('*************************************************')
        print('Password change successful.')
        print('*************************************************')
        interlude(user)
    else:
        print("Passwords don't match. Please try again")
        passChange(user)
        

def makeComplaint(user):
    complaint=input('What is your complaint? \n')
    user.apend(complaint)
    print('*************************************************')
    print('Your complaint has been noted. Thank you')
    print('*************************************************')
    interlude(user)

def logout(user):
    logoutBool = int(input('Do you want to log out of your account? 1. Yes. 2. No \n'))
    if(logoutBool==1):
        print('You have successfully logged out of your account')
        print("**************************************** \n")
        
    elif(logoutBool==2):
        accountMenu(user)
    else:
        print('Please select a valid option')
        logout(user)