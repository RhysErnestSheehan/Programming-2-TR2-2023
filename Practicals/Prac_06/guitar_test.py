from Prac_06.guitar import Guitar


def main():
    # Asks the user for information about a guitar
    print("Enter the guitars information")
    name = input("name:")
    year = input("year:")
    cost = input("cost:")

    # creates a list with the name, year and cost to make a guitar object
    guitar = [name, year, cost]


main()
