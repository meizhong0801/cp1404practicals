from musician import Musician


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({str(self.musicians)})"

    def add(self, musician):
        """Add a musician to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Display musician with its instrument."""
        for musician in self.musicians:
            print(musician.play())