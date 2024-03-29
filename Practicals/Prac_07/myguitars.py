class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : {self.cost})"


def main():
    infile = open("guitars.csv", 'r')
    guitars = []
    # Add guitars to guitar lists
    for line in infile:
        guitar = []
        line = line.strip()  #
        parts = line.split(',')
        Guitar.name = parts[0]
        Guitar.year = parts[1]
        parts[1] = int(parts[1])
        Guitar.cost = parts[2]
        guitar.append(Guitar.name)
        guitar.append(Guitar.year)
        guitar.append(Guitar.cost)
        guitars.append(guitar)
    print(guitars)
    # Gets guitars from the user, creates a guitar list for each guitar and add them to the guitars list
    number_of_guitars = int(input("How many guitars do you have? "))
    for new_guitars in range(number_of_guitars):
        name = input("Name: ")
        year = int(input("year: "))
        cost = float(input("cost: "))
        guitar.append(name)
        guitar.append(year)
        guitar.append(cost)
        guitars.append(guitar)
    outfile = open("guitars.csv", "w")
    for new_guitar in guitars:
        print(new_guitar, file=outfile)
    print(guitars)
    infile.close()

# This was as far as I got. I couldn't figure out how to strip the list before or after saving it to the file.


main()
