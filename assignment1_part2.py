
class Book:
    def __init__(self, author = "", title = ""):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ", written by " + self.author)


if __name__ == "__main__":
    Book_One = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    Book_Two = Book("Walter Scott", "Ivanhoe: A Romance")
    Book_One.display()
    Book_Two.display()