"""CP1404 Rhys Sheehan Prac 01 menus"""

name = input('What is you name?')
MENU = "Menu:\n Q - Quit\n H - Hello \n G - Goodbye"
print(MENU)
choice = input('What is your choice?').upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("invalid menu choice")
    print(MENU)
    choice = input('What is your choice?')
print('Thanks for playing')