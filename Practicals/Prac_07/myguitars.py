class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : {self.cost})"


def main():
    infile = open("guitars.csv", 'r')
    guitar = []
    for line in infile:
        line = line.strip()  #
        parts = line.split(',')
        parts[1] = int(parts[1])
        guitar.append(parts)
    print(guitar)
    infile.close()
    guitar.sort()


main()
