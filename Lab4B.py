# Class: CSE 1321L
# Section: 16B
# Term: Fall 2026
# Instructor: Rubaina Roshan
# Name: Abiegail Raymond
# Lab: Lab 4B

# Program Lab4B.py

#additive inverse of 5 -> -5
#case 0:
    #additive_inverse = -1 * number
#reciproal (use if statement for 0)
    #else = find reciprcroal
#exponent number ** 2 or 3

#choice = input("
#match choice:
#case
    #print

print("Welcome!")
user_number = float(input("Please input a number: "))

print()#

print("What would you like to do with this number:")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")

choice = int(input(""))

print()#

match choice:
    case 0:
        case0 = round(-user_number, 3)
        print("The additive inverse of", user_number, "is ", case0)
    case 1:
        if user_number == 0:
            print("Cannot divide by 0!")
        else:
            reciprocal = round(1 / user_number, 3)
            print("The reciprocal of", user_number, "is", reciprocal)
    case 2:
        square = round(user_number ** 2, 3)
        print("The square of", user_number, "is ", square)
    case 3:
        cube = round(user_number ** 3, 3)
        print("The cube of", user_number, "is ", cube)
    case 4:
        print("Thank you, goodbye!")

    case _:
        print("Invalid option!")

