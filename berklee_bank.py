bank_dict = {

    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},

}





'''
Task: Welcomes user, and check if the pin  and name is valid and goes together. If not, denied.
Name: check_valid
Input: n/a
Side Effects: Welcomes, and if not valid denied.
Return: bool
'''

'''
Task: Prints all of the commands we can do. 
Name: print_menu
Input: n/a
Side Effects: Deposit, Withdraw, Balace, Quit
Return: userinput
'''

'''
Task: Adds user input into their balance. 
Name: deposit
Input: n/a
Side Effects: n/a
Return: n/a
'''

'''
Task: withdrawl money from the balace if valid.
Name: withdrawl
Input: n/a
Side Effects: n/a
Return: n/a
'''

'''
Task: shows how much money the user has.
Name: balance
Input: n/a
Side Effects: Prints the balanced
Return: n/a
'''

'''
Task: Quits the command.
Name: quit
Input: n/a
Side Effects: n/a
Return: n/a
'''

def run_test():
    withdrawl("Priya") # Ask for amount, if 200 fail.
    withdrawl("Priya") # Ask for amount, if 100 succeed.

    deposit("Priya") # Asks for amount, if 100 should succeed.

    balance("Priya") # print 100.

    check_valid() # Expecting True if user input valid, and False if not.
    