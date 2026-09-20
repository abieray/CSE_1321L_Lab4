# Class: CSE 1321L
# Section: 16B
# Term: Fall 2026
# Instructor: Rubaina Roshan
# Name: Abiegail Raymond
# Lab: Lab 4C

# Program Lab4C.py

first_side = float(input("Enter the first side of the triangle: "))
second_side = float(input("Enter the second side of the triangle: "))
third_side = float(input("Enter the third side of the triangle: "))

if first_side > 0 and second_side > 0 and third_side > 0:
    if first_side + second_side > third_side and first_side + third_side > second_side and second_side + third_side > first_side:
        if first_side == second_side and second_side == third_side:
            print("The triangle is an equilateral triangle.")
        elif first_side == second_side or first_side == third_side or second_side == third_side:
            print("The triangle is an isosceles triangle.")
        else:
            print("The triangle is a scalene triangle.")
    else:
        print("The sides do not form a valid triangle.")
else:
    print("Invalid input. All sides must be greater than 0.")