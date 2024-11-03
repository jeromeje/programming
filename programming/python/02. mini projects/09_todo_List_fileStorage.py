
# ToDo List :


def add_task(fileName):

    task = input("Enter New Task : ")

    with open(fileName,'a') as file:

        file.write(f"{task}\n")

    print("Task Added Successfully..!")


def view_tasks(fileName):

    with open(fileName,'r') as file:

        tasks =file.readlines()

        if tasks:
            print("Tasks : ")

            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task.strip()}")

        else:
            print("No Tasks Available..!")


def remove_task(fileName):

    view_tasks(fileName)

    task_no = int(input("Enter the Task Number to Mark as Done : "))

    with open(fileName,'r') as file:
        tasks = file.readlines()

    with open(fileName,'w') as file:
        
        for i , task in enumerate(tasks,start=1):

            if i !=  task_no: 
                file.write(task)

    print("Your Task Marked as Done.")


File_Name = "todo.txt"

while True :
    
    choice = input("1. Add Task\n2. View Task\n3. Remove Task\n4. Exit\nEnter the Option : ")

    if choice == "1":
        add_task(File_Name)

    elif choice == "2":
        view_tasks(File_Name)

    elif choice == "3":
        remove_task(File_Name)

    elif choice == "4":
        break

    else:
        print("Invalid Choice. Please Try Again.")

