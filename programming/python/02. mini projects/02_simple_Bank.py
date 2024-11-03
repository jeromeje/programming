
# Simple Banking Project :


balance = 500


while True:

    print("\n Welcome to The Simple Banking System..!")

    print(" 1 - Deposit ")
    print(" 2 - Withdraw ")
    print(" 3 - Check Balance ")
    print(" 4 - Exit ")

    choice = input("Choose Your Option [ 1 - 4 ] : ")

    if choice == "1":

        amount = float(input("Enter Your Deposit Amount : "))

        balance += amount

        print(f"${amount} Deposited Successfully..!")

    
    elif choice == "2":

        amount = float(input("Enter Amount to Withdraw : "))

        if amount <= balance:
            balance -= amount

            print(f"${amount} Withdrawn Successfully..!")

        else:
            print("Insufficient Balance..!")

    elif choice == "3" :

        print(f"Your Current Balance is ${balance}.")

    elif choice == "4" :

        print("Existing the System. Have a Nice Day..!")
        break


    else :
        print("Invalid Option..! Please Choose Correct Option..!")


