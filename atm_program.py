#atm program
# account with username and password -->login
# menu of options - view balance, deposit, withdraw, quit
# the menu is going to keep popping up until you hit quit

# set the account variables for the ATM
#homeslice@hotmail.com
username = 'hsimpson@gmail.com'
password = 'swordfish'
balance = 100
login = False

print('Welcome to our ATM!')

# begin login loop
while login==False:
    print('Enter username')
    usr=input()
    print('Enter password')
    pswd=input()
# if both are correct, exit login loop and enter menu loop
    if usr == username and pswd == password:
        login=True
        break
    elif usr != username or pswd != password:
        print('Incorrect username or password!')
        print('Would you like to retry? (y/n)')
        retry = input()
        if str(retry) == 'n':
            print('Goodbye!')
            break
    
# begin menu loop
while login==True:
    print('What would you like to do?')
    print('1. View Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    # capture menu response
    response = input()

    # view balance conditional statement
    if str(response) == '1':
        print('Your balance is $' + str(balance))
    # deposit conditional statement
    if str(response) == '2':
        print('How much would you like to deposit?')
        deposit = input()
        balance = int(balance) + int(deposit)
        print('Your new balance is $' + str(balance))
    # withdraw conditional statement
    if str(response) == '3':
        print('How much would you like to withdraw?')
        withdrawl = input()
        balance = int(balance) - int(withdrawl)
        print('Your new balance is $' + str(balance))
    # exit option breaks out of the menu loop
    if str(response) == '4':
        print('Thank you for using our ATM!')
        login = False
        break
    # error handling for the responses
    else:
        print('Option not recognized. Please enter the number for your option!')
