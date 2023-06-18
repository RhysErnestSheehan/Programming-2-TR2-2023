"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# A ValueError will occur when the numerator or denominator is not a valid number,
# eg. if the user enters 0 or a letter.

# A ZeroDivisionError will occur when the user enters zero as the denominator

# Yes you coud change the code to avoid the possibility of a ZeroDivisionError by adding error checking
# so if the user tries to divide by zero it asks them to enter a number that is not zero
