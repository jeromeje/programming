
# Grocery  Shop :


import grocery_operations as go

while True:

    print("\n1. Add Items")
    print("2. Remove Items")
    print("3. View Items")
    print("4. Display Total Cost")
    print("5. Exit")


    choice = input("Enter Your Choice : ")

    if choice == "1" :

        name = input("Enter Product Name : ")
        price = float(input("Enter Product Price : "))

        go.Add_items(name,price)

    elif choice == "2" :
        
        name = input("Enter Product Name : ")

        go.Remove_items(name)


    elif choice == "3" :
        
        go.Display_items()


    elif choice == "4" :
        
        go.Total_cost()


    elif choice == "5" :
        
        print("Exit the program...")
        break

    else:
        print("Invalid Choice...")

