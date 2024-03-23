#Bank Teller App

#Step 1 - Initalize variables
#initalizing two variables that can be used in the app and setting them to 0
checking_balance = 0
savings_balance = 0

#Step 2 - Return the balance that the customer has in the bank
#create a function that checks balances with 3 account types as the parameters
def check_balance(account_type, checking_balance, savings_balance):
#account_type param is a string that can either be "savings" or "checking"
    if account_type == "savings":
        #setting the new above variable balance to the value of savings balance
        balance = savings_balance
    elif account_type == "checking":
        balance = checking_balance
    #don't need to list account type here because it's an else statement
    else:
        return "Unsucessful, please enter \"checking\" or \"savings\""
    balance_statement = "Your " + account_type + " balance is " + str(balance) + ".\n"
    return balance_statement

#printing check balance for checking
print(check_balance('checking', checking_balance, savings_balance))
#printing check balance for savings
print(check_balance('savings', checking_balance, savings_balance))

#Step 3 - Allow the customer to make a deposit to their bank account
#amount is the amount that's going to be deposited
def make_deposit(account_type, amount, checking_balance, savings_balance):
    #creating a variable deposit status and setting it to an empty string
    deposit_status = ''
    #can have a double if statement here. First check is to make sure amount is greater than 0
    if amount > 0:
        if account_type == "savings":
            # += operator adds to and then updates the amount variable
            savings_balance += amount
            deposit_status = "successful"
        elif account_type == "checking":
            checking_balance += amount
            deposit_status = "successful"
            #else of an error statement
        else:
            deposit_status = "Unsucessful, please enter \"checking\" or \"savings\""
    else:
        deposit_status = 'unsucessful, please enter an amount greater than 0'
        #assigning to the deposit_statement variable
    deposit_statement = 'deposit of ' + str(amount) + 'to your ' + account_type + 'account was ' + deposit_status + '.'
    print(deposit_statement)
    #return savings and checking balances each time the make deposit function is run
    return savings_balance, checking_balance

#calling make deposit function to update bank account after savings deposit of $10
savings_balance, checking_balance = make_deposit("savings", 10, checking_balance, savings_balance)

#printing the savings balance
print(check_balance("savings", checking_balance, savings_balance))

#calling make deposit function to update bank account after checking deposit of $200
#assign the function call to the checking_balance and savings_balance
checking_balance, savings_balance = make_deposit("checking", 200, checking_balance, savings_balance)

#now calling check_balance to get an updated balance
print(check_balance("checking", checking_balance, savings_balance))

#Step 4 - Allow the customer to make a withdrawal to their bank account




#Step 5 - Allow the customer to decide whether to make the transaction with checking or savings account



#Step 6 - Allow the customer to make a transfer between savings and checking account