MENU = "Menu:\n (L)oad Projects\n (S)ave Projects\n (D)isplay Projects\n (F)ilter projects by date\n (A)dd new project\n (U)pdate project\n (Q)uit\n"


def main():
    print("Project Management - by Rhys Sheehan")
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            load_projects(projects)
        elif choice == 'S':
            save_projects()
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            pass
        elif choice == 'A':
            add_project(projects)
        elif choice == 'u':
            pass
        else:
            print("Please choice a vaild choice from the menu")
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'Q':
            print("Have a nice day. :)")


def load_projects(projects):
    input_filename = input("Enter the name of a projects file: ")
    in_file = open(input_filename, 'r')
    in_file.readline()
    for line in in_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        parts[4] = float(parts[4])
        projects.append(parts)
    in_file.close()
    return projects


def save_projects(projects):
    output_filename = input("Enter the name of a projects file: ")
    out_file = open(output_filename, 'w')
    for project in projects:
        print(project, file=out_file)
    out_file.close()


def display_projects(projects):
    print("incomplete Projects")
    for project in projects:
        if projects[3] > 100:
            print(project)


def filter_by_data():
    pass


def add_project(projects):
    print("Let's add a new project")
    project = []
    name = input("Name: ")
    start_data = input("Start data: ")
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = float(input("Percent complete: "))
    project.append(name)
    project.append(start_data)
    project.append(cost_estimate)
    project.append(percent_complete)
    projects.append(project)
    return projects


def update_project():
    pass


main()
