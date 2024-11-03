
# ATM in Exception Handling :



balance = 1000  # User Account Balance


try:

    withdrawal_amount = int(input("Enter The Amount to Withdraw : ")) #Asking for input

    if withdrawal_amount > balance:

        raise ValueError("Insufficient Balance") # Manually raising an Exception
    
    if withdrawal_amount <= 0:

        raise ValueError("Amount Must be Greater than Zero") # exception for invalid input
    
    balance -= withdrawal_amount
    print("Withdrawal Successful. Remaining Balance is : ", balance)

except ValueError as e:
    print("Error : ", e) #handling exceptions by printing the msg

finally:
    print("Thank You For Using The ATM.")