
class Book:
    def __init__(self, title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    def __str__(self):
        status = "Dostępna." if self.available else "Nie dostępna."
        return f"\nTytuł: {self.title}\nAutor: {self.author}\nRok wydania: {self.year}\nDostępność: {status}"
    def borrow(self):
        if self.available:
            self.available = False
            print(f'Wypożyczono {self.title}.')
        else:
            print(f'Książka {self.title} nie jest dostępna na ten moment.')
    def return_book(self):
        if not self.available:
            self.available = 'True'
            print(f'Zwrócono książkę {self.title}.')
        else:
            print(f'Nie wypożyczano książki {self.title} dlatego nie może być zwrócona.')

class Library:
    def __init__(self, books = []):
        self.books = books
    def __str__(self):
        if self.books:
            return '\nW bibliotece znajdują się następujące książki: \n'.join([str(book) for book in self.books])
        else:
            return 'Biblioteka jest pusta.'
    def add_book(self, book: 'Book'):
        self.books.append(book)
        print(f'Książka o tytule {book.title} została dodana do biblioteki.')
    def search_by_title(self, title):
        foundBooks = []
        print(f'Odnalezione książki dla wszukanego tytułu: "{title}": ')
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                foundBooks.append(book)
        return foundBooks
    def search_by_author(self, author):
        print(f'Odnalezione książki dla wszukanego autora: "{author}": ')
        foundBooks = []
        for book in self.books:
            if author.lower() in book.author.lower():
                print(book)
                foundBooks.append(book)
        return foundBooks
book = Book('Tytuł1', 'Autor1 Aa', '1940')
book2 = Book('Tytuł B', 'Autor2 Aa', '1945')
book3 = Book('Tytuł 3C', 'Autor3 Aa', '1960')
print(book)
book.borrow()
books = [book,book2]

library = Library(books)
print(library)
library.add_book(book3)
searchResultTitle = library.search_by_title('Tytuł')
searchResultAuthor = library.search_by_author('Autor')