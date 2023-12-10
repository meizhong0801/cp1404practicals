"""Build class ProgrammingLanguage"""


class ProgrammingLanguage:
    """Represent a programing language object"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing.title() == 'Dynamic'

    