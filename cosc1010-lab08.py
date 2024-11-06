# Caleb Behrman
# UWYO COSC 1010
# 11/6/24
# Lab 8
# Lab Section: 10


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

#this one is going to take a second hahahah
#I dont know if we have learned about importing math or not, I know about this from highschool, but this just makes it to where there more things that you can do with math in the code
import math

def convert_string(s):
    try:
        #Convert to float first
        value=float(s)
        #If it has a decimal point, it is a float, but we check for only one decimal place
        if '.' in s and s.count('.')==1:
            return value
        #If no decimal point, return as integer
        elif '.' not in s:
            return int(value)
        else:
            return False
    except ValueError:
        #returns faslse if integers or whatever else cant be obtained
        return False

#This is the function y = mx + b for a range of x
def slope_intercept(m, b, x_lower, x_upper):
    #This makes sure that everything is just an interger
    if not isinstance(m, (int, float)) or not isinstance(b, (int, float)):
        return False
    if not isinstance(x_lower, int) or not isinstance(x_upper, int):
        return False
    if x_lower>x_upper:
        return False
    
    result=[]
    for x in range(x_lower, x_upper+1):
        y=m*x+b
        result.append(y)
    return result

#This is the function to solve quadratic formula
def quadratic_formula(a, b, c):
    #This checks if a is 0 to avoid division by zero
    if a==0:
        return False

    discriminant=b**2-4*a*c
    if discriminant<0:
        return None
    
    #This calculatess the 2 solutions using the quad. form
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    return root1, root2

#To calculate the square root, return None if negative
def safe_sqrt(x):
    if x < 0:
        return None
    return math.sqrt(x)

#The main interaction with the person messing with the code is here
def main():
    while True:
        print("*" * 75)
        print("Enter 'exit' to quit the program.")

        # Get input for slope_intercept
        m_input=input("Enter the slope (m): ")
        if m_input.lower()=="exit":
            break
        m=convert_string(m_input)

        b_input=input("Enter the intercept (b): ")
        if b_input.lower()=="exit":
            break
        b=convert_string(b_input)

        x_lower_input=input("Enter the lower bound of x: ")
        if x_lower_input.lower()=="exit":
            break
        x_lower=convert_string(x_lower_input)

        x_upper_input=input("Enter the upper bound of x: ")
        if x_upper_input.lower() == "exit":
            break
        x_upper=convert_string(x_upper_input)

        if m is False or b is False or x_lower is False or x_upper is False:
            print("Invalid input, please try again.")
            continue

        result=slope_intercept(m, b, x_lower, x_upper)
        if result is False:
            print("Error in calculating slope-intercept.")
        else:
            print(f"Calculated y-values for x from {x_lower} to {x_upper}: {result}")

        print("*" * 75)

        #This code gets an input from the people using this code
        a_input=input("Enter the coefficient a (for quadratic formula): ")
        if a_input.lower()=="exit":
            break
        a=convert_string(a_input)

        b_input=input("Enter the coefficient b (for quadratic formula): ")
        if b_input.lower()=="exit":
            break
        b=convert_string(b_input)

        c_input=input("Enter the coefficient c (for quadratic formula): ")
        if c_input.lower()=="exit":
            break
        c=convert_string(c_input)

        if a is False or b is False or c is False:
            print("Invalid input for quadratic coefficients, please try again.")
            continue

        roots = quadratic_formula(a, b, c)
        if roots is False:
            print("Coefficient 'a' cannot be zero in a quadratic equation.")
        elif roots is None:
            print("No real solutions (discriminant is negative).")
        else:
            print(f"The roots of the quadratic equation are: {roots}")

        print("*" * 75)

        #this gets the imput for the square roots
        sqrt_input=input("Enter a number to take the square root of: ")
        if sqrt_input.lower()=="exit":
            break
        num=convert_string(sqrt_input)

        if num is False:
            print("Invalid input, please try again.")
            continue

        sqrt_result=safe_sqrt(num)
        if sqrt_result is None:
            print("Cannot calculate the square root of a negative number.")
        else:
            print(f"The square root of {num} is: {sqrt_result}")

if __name__=="__main__":
    main()