def menu():
    print("-------------------Main Menu----------------------")
    print("Select from the menu below \n")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Overall Profit")
    print("5. Quit")

username = 1122 #roll number
password = "password"
Balance = 1245.50
print("----------------Enter Account Details-----------------")
var_user = int(input("Enter Account Number : "))
var_password = input("Enter Password : ")
print("------------------------------------------------------")
if ( username == var_user and password == var_password):
    quit = 'Y'

    while(quit == 'Y' or quit == 'y'):
        menu()
        choice = int(input("Enter Choice : "))
        if choice == 1:
            print("User balance : " + str(Balance))
        elif choice == 2:
            Deposit = int(input("Enter amount to Deposit : "))
            profit = Deposit * 0.12
            Balance += Deposit
            print("Profit on deposited amount : " + str(profit))
        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw : "))
            if ( withdraw > Balance):
                print("Not enough funds")
            else:
                Balance -= withdraw
                print("Amount withdrawn Successfully")
        elif choice == 4:
            interest = 0.14 * Balance
            print("Interest : " + str(interest))
        elif choice == 5:
            break
        else:
            print("Invalid Input")
        quit = input("Do you want to continue (Y/N) : ")
else:
    print("Wrong Username or Password")