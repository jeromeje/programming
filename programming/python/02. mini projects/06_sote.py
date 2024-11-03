

# User Registration Projcet :

def register_user(fileName):

    userName = input("Enter UserName : ")
    password = input("Enter Password : ")

    with open(fileName,'a') as file:

        file.write(f"{userName},{password}\n")

    print("User Registered Successfully..!")


def login_user(fileName):

    userName = input("Enter UserName : ")
    password = input("Enter Password : ")

    with open(fileName,'r') as file:

        users = file.readlines()

        for user in users:

            stored_username,stored_password = user.strip().split(',')

            if stored_username == userName and stored_password == password:

                print("Login Successfully..!")
                
                return

    print("Login Failed..! \nInvalid Credentials..!")


File_Name = "Users.txt"

while True:

    choice = input("1. Register\n2. Login\n3. Exit\n Enter Your Option : ")

    if choice == "1":
        register_user(File_Name)

    elif choice == "2":
        login_user(File_Name)

    elif choice == "3":
        break

    else:
        print("Invalid Choice. Please Try Again.")


