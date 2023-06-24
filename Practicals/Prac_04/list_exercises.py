"""Rhys Sheehan CP1404 practical 4 list exercises"""

numbers = []
for i in range(5):
    numbers_picked = int(input("Number: "))
    numbers.append(numbers_picked)
print(f"The first number is {numbers[0]}.")
print(f"The last number is {numbers[4]}.")
print(f"The smallest number is {min(numbers)}.")
print(f"The largest number is {max(numbers)}.")
