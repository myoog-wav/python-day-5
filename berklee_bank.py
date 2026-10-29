bank_dict = {

    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},

}

def check_valid(name, pin):
    '''
    Task: Welcomes user, and check if the pin  and name is valid and goes together. If not, denied.
    Name: check_valid
    Input: n/a
    Side Effects: Welcomes, and if not valid denied.
    Return: bool
    '''
    

    if bank_dict.get(name):
        user_values = bank_dict.get(name)
        if pin == user_values.get("pin"):
            return True
        return False
    
        

def print_menu():
    '''
    Task: Prints all of the commands we can do. 
    Name: print_menu
    Input: n/a
    Side Effects: Deposit, Withdraw, Balace, Quit
    Return: userinput
    '''
    choice = input("Do you want to deposit, withdrawl, balance, or quit?")
    return choice

def deposit(name):
    '''
    Task: Adds user input into their balance. 
    Name: deposit
    Input: n/a
    Side Effects: n/a
    Return: n/a
    '''

    deposit_amount = int(input("How much would you like to disposit? "))
    if bank_dict.get(name):
        user_values = bank_dict.get(name)
        previous_bal = user_values.get('balance')
        new_bal = previous_bal + deposit_amount
        user_values.update({"balance": new_bal}) 



def withdrawl(name):
    '''
    Task: withdrawl money from the balace if valid.
    Name: withdrawl
    Input: n/a
    Side Effects: n/a
    Return: n/a
    '''  
    if bank_dict.get(name):
            withdrawl_amount = int(input("How much would you like to take out? "))
            user_values = bank_dict.get(name)
            previous_bal = user_values.get('balance')
            new_bal = previous_bal - withdrawl_amount
            if new_bal < 0:
                print("Insuffocoent funds")
            else:
                user_values.update({"balance": new_bal}) 


    return

def balance(name):
    '''
    Task: shows how much money the user has.
    Name: balance
    Input: n/a
    Side Effects: Prints the balanced
    Return: n/a
    '''
    if bank_dict.get(name):
        user_values = bank_dict.get(name)
        amount = user_values.get("balance")
        print(amount)
  

    return

def quit():
    '''
    Task: Quits the command.
    Name: quit
    Input: n/a
    Side Effects: n/a
    Return: n/a
    '''
    return

def run_test():
    withdrawl() # Ask for amount, if 200 fail.
    withdrawl() # Ask for amount, if 100 succeed.

    deposit() # Asks for amount, if 100 should succeed.

    balance() # print 100.

    check_valid() # Expecting True if user input valid, and False if not.



def main():

    print("Welcome")

    user_name = input("What is your name? ")
    user_pin = input('What is your pin? ')

    valid = check_valid(user_name, user_pin)
    if not valid:
        print("Invalid...")
        return

    while True:
        users_choice = print_menu()
        if users_choice == "balance":
            balance(user_name)
        elif users_choice == "withdrawl":
            withdrawl(user_name)
        elif users_choice == "quit":
            break
        elif users_choice == "deposit":
            deposit(user_name)
        else:
            print("You can't do that...")

    
main()