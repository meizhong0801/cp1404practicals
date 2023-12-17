"""
load, display, filter, add, unpdate, and save projects
15 hours
"""

import datetime
from operator import attrgetter

from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Main function to manage the project management system."""

    print(MENU)
    choice = input(">>> ").upper()
    while choice not in list("LSDFAUQ"):
        print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()

    projects = load_projects()  # Load existing projects from a file
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_project(projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_project_by_date(projects, date_str)
        elif choice == "A":
            projects = add_new_project(projects)
        elif choice == "U":
            undate_project(projects)
        print(MENU)
        choice = input(">>> ").upper()


def load_projects():
    """Read file of project details, save as objects."""

    projects = []
    # Open the file for reading
    in_file = open('projects.txt', 'r')
    # File format is like: Name, Start date, Priority, Estimate cost, Completion
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are project data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts
        parts = line.strip().split('\t')
        # print(parts)  # debugging
        # Construct a Project object using the elements
        # priority and completion percentage should be an int, estimate cost should be float.
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        # Add the project we've just constructed to the list
        projects.append(project)
    # Close the file as soon as we've finished reading it
    in_file.close()

    return projects


def display_project(projects):
    """Display incomplete and completed projects separately. """

    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.completion_percentage < 100:
            incomplete_projects.append(project)
        else:
            complete_projects.append(project)

    incomplete_projects.sort()  # Sort incomplete projects
    complete_projects.sort()  # Sort completed projects

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(project)

    print("Completed projects: ")
    for project in complete_projects:
        print(project)


def filter_project_by_date(projects, date_str):
    """Filter projects that start after a given date and display them."""

    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = []
    for project in projects:
        if project.start_date > date:
            filtered_projects.append(project)
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Add a new project to the list of projects."""

    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    complete = float(input("Percent complete: "))
    project = Project(name, start_date, priority, cost, complete)
    projects.append(project)

    return projects


def undate_project(projects):
    """Update an existing project's completion percentage and priority."""

    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    projects[choice].completion_percentage = new_percentage
    projects[choice].priority = new_priority

    return projects


def save_project(projects):
    """Save project details to a file."""

    out_file = open('projects.txt', 'w')
    out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
    for project in projects:
        out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


main()

