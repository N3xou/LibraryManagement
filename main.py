# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Book:
    def __init__(self, title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    def __str__(self):
        status = "Dostępna." if self.available else "Nie dostępna."
        return f"Tytuł: {self.title}\nAutor: {self.author}\nRok wydania: {self.year}Dostępność: {status}"
    def borrow(self):
        if self.available:
            self.available = False
            return f'Wypożyczono "{self.title}".'
        else:
            return f'Książka {self.title} nie jest dostępna na ten moment.'
    def return_book(self):
        if not self.available:
            self.available = 'True'
            return f'Zwrócono książkę {self.title}.'
        else:
            return f'Nie wypożyczano książki {self.title} dlatego nie może być zwrócona.'

book = Book('Tytuł1', 'Autor1 Aa', '1940')
print(book)
book.borrow()