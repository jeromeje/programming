
# Employee Management Project :

"""
1. Add Employee
2. Romove Employee
3. Update Employee
4. Display Employee
5. Save to File
6. Load to File
7. Exit
"""

# Excute the code Here :

Employees = {}

def add_employee(emp_id,name,age,department,salary):

    Employees[emp_id] = {
        "Name": name,
        "Age": age,
        "Department": department,
        "Salary": salary
    }

    print(f"Employee {name} added Successfully..!")


def view_employee():

    if Employees:
        for emp_id, emp_data in Employees.items():
            print(f"Employee ID : {emp_id} ==> Details : {emp_data}")

    else:
        print("No Employees Available..!")


def remove_employee(emp_id):

    # try:
        emp = Employees.pop(emp_id)
        print(f"Employee {emp['Name']} removed Successfully..!")


while True:

    print("\n Welcome To Employee Management System : ")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Display Employee")
    print("5. Save to File")
    print("6. Load to File")
    print("7. Exit")


    choice = input("\nEnter Your Option : ")


    if choice == "1":
        
        emp_id = input("Enter Employee ID : ")
        name = input("Enter Employee Name : ")
        age = input("Enter Employee Age : ")
        department = input("Enter Employee Department : ")
        salary = input("Enter Employee Salary : ")

        add_employee(emp_id,name,age,department,salary)


    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        view_employee()

    elif choice == "5":
        pass

    elif choice == "6":
        pass

    elif choice == "7":
        break

    else:
        print("Invalid Option. Please Try Again.")

