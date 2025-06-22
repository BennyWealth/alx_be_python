
class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to notify when a book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous representation of the book (used for debugging)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
