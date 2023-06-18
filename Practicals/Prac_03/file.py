"""Rhys Sheehan CP1404 Prac 3 files.py"""
OUTPUT_FILE = 'name.txt'
out_file = open(OUTPUT_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

INPUT_FILE = 'name.txt'
in_file = open('name.txt', "r")
name = in_file.readline().strip()
print(f"Your name is {name}")
in_file.close

INPUT_FILE = 'numbers.txt'
in_file = open('numbers.txt', "r")
line1 = int(in_file.readline())
line2 = int(in_file.readline())
in_file.close
print(line1 + line2)

