"""
project class with tests.
"""

import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority


def run_tests():
    """Run simple tests/demos on Project class."""
    project_01 = Project("organise pantry", "20/07/2022", 1, 25, 55)
    project_02 = Project("build car park", "12/09/2021", 2, 600000, 95)
    project_03 = Project("mow lawn", "31/10/2022", 3, 3, 0)

    projects = [project_01, project_02, project_03]
    print(project_01)
    projects.sort()  # Sort the projects based on priority.

    for project in projects:
        print(project)

    earlist = project_03
    for project in projects:
        # Find the project with the earliest start date.
        if project.start_date < earlist.start_date:
            earlist = project
    print(f"The earlist projects is {earlist.name}")


if __name__ == "__main__":
    run_tests()


