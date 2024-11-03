
""" 

# Pizza order and bill generation :


"""
small_pizza = 15

medium_pizza = 20

large_pizza = 25

# --------------------


add_pepper_small_pizza = 2

add_pepper_large_or_Medium_size = 3

add_Cheese_any_size = 1

#-----------------------


size = input("What size of Pizza Do you Want? [ S / M / L ] ")

add_pepper = input("Do you Want Pepper? [ Y / N ] ")

add_extra_cheese = input("Do you Want Extra Cheese? [ Y / N ] ")


bill = 0

if size == "S":

    bill += small_pizza

elif size == "M":

    bill += medium_pizza

elif size == "L":

    bill += large_pizza

else:

    print("Invalid Input")



if add_pepper == "Y":

    if size == "S":
        bill += add_pepper_small_pizza

    else:
        bill += add_pepper_large_or_Medium_size



if add_extra_cheese == "Y":

    bill += add_Cheese_any_size



print(f"Your final Bill is ${bill}")

