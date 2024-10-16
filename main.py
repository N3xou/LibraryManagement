class Book:
    def __init__(self, title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    def __str__(self):
        status = "Dostępna." if self.available else "Wypożyczona."
        return f"Tytuł: {self.title}\nAutor: {self.author}\nRok wydania: {self.year}\nDostępność: {status}\n"
    def borrow(self):
        if self.available:
            self.available = False
            print(f'Wypożyczono:\n{self.__str__()}.')
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
    def search_by_title(self, title, info = False):
        foundBooks = []
        if info:
            print(f'Odnalezione książki dla wszukanego tytułu: "{title}": ')
        for book in self.books:
            if title.lower() in book.title.lower():
                if info:
                    print(book)
                foundBooks.append(book)
        return foundBooks
    def search_by_author(self, author, info = False):
        if info:
            print(f'Odnalezione książki dla wszukanego autora: "{author}": ')
        foundBooks = []
        for book in self.books:
            if author.lower() in book.author.lower():
                if info:
                    print(book)
                foundBooks.append(book)
        return foundBooks
    def list_available_books(self):
        print('Tytuły dostępne do wypożyczenia')
        for book in self.books:
            if book.available:
                print(book.title)
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print('Biblioteka nie posiada takiej książki. Sprawdź pisownie tytułu.')
    def borrow_book2(self, title):
        foundBooks = self.search_by_title(title)
        if len(foundBooks) == 1:
            confirmation = int(input(f'{foundBooks[0]}\nCzy chcesz wypożyczyć powyższą książkę\n[0] Tak\n[1] Nie\n'))
            if confirmation == 0:
                foundBooks[0].borrow()
            else:
                return
        elif len(foundBooks) > 1:
            idx = 0
            print('Odnaleziono więcej niż jedną książkę o wybranym tytule. Proszę wybrać z listy: ')
            for book in foundBooks:
                if book.available:
                    print(f'Indeks [{idx}]\n{book}')
                    idx+=1
            inputIdx = int(input('Proszę wpisać numer indeksu pożądanej ksiązki: '))
            while inputIdx > idx-1 or idx < 0:
                inputIdx = int(input('Niepoprawny index proszę spróbować ponownie: '))
            foundBooks[idx].borrow()
        else:
            print('Biblioteka nie posiada takiej książki. Sprawdź pisownie tytułu.')
    def return_book(self, title):
        foundBooks = self.search_by_title(title)
        if len(foundBooks) == 1:
            confirmation = int(input(f'{foundBooks[0]}\nCzy chcesz oddać powyższą książkę\n[0] Tak\n[1] Nie\n'))
            if confirmation == 0:
                foundBooks[0].return_book()
            else:
                return
        elif len(foundBooks) > 1:
            idx = 0
            print('Odnaleziono więcej niż jedną książkę o wybranym tytule. Proszę wybrać z listy: ')
            for book in foundBooks:
                if not book.available:
                    print(f'Indeks [{idx}]\n{book}')
                    idx += 1
            inputIdx = int(input('Proszę wpisać numer indeksu zwracanej książki: '))
            while inputIdx > idx - 1 or idx < 0:
                inputIdx = int(input('Niepoprawny index proszę spróbować ponownie: '))
            foundBooks[idx].return_book()
        else:
            print('Biblioteka nie rozpoznaje takiej książki. Sprawdź pisownie tytułu.')

class LibraryApp:
    def __init__(self):
        book1 = Book('Lalka', 'Bolesław Prus', 1890)
        book2 = Book('Pan Tadeusz', 'Adam Mickiewicz', 1834)
        book3 = Book('Ferdydurke', 'Witold Gombrowicz', 1937)
        self.library = Library([book1,book2,book3])
    def run_library(self):
        exit_program = False

        while not exit_program:
            print('Witaj w bibliotece, poniżej znajdziesz dostępne opcje:')
            print('[1] Dodaj książkę do biblioteki.')
            print('[2] Wyszukaj książkę w bibliotece po tytule.')
            print('[3] Wyszukaj książkę w bibliotece po autorze.')
            print('[4] Wyświetl dostępne książki.')
            print('[5] Wypożycz książkę.')
            print('[6] Zwróć książkę.')
            print('[7] Wyjdź z programu.')
            option = int(input('Wprowadź swój wybór opcji: '))
            if option == 1:
                titleToAdd = input('Podaj tytuł książki: ')
                authorToAdd = input('Podaj autora książki: ')
                yearToAdd = int(input('Podaj rok wydania książki: '))
                bookToAdd = Book(titleToAdd, authorToAdd, yearToAdd)
                self.library.add_book(bookToAdd)
            elif option == 2:
                titleToSearch = input('Podaj tytuł szukanej książki: ')
                self.library.search_by_title(titleToSearch, info=True)
            elif option == 3:
                authorToSearch = input('Podaj autora szukanej książki: ')
                self.library.search_by_author(authorToSearch, info=True)
            elif option == 4:
                self.library.list_available_books()
            elif option == 5:
                titleToBorrow = input('Podaj tytuł książki którą chcesz wypożyczyć: ')
                self.library.borrow_book2(titleToBorrow)
            elif option == 6:
                titleToReturn = input('Podaj tytuł książki którą chcesz zwrócić: ')
                self.library.return_book(titleToReturn)
            elif option == 7:
                exit_program = True
            else:
                print('Wybrano niepoprawny numer, spróbuj jeszcze raz.\n')


if __name__ == "__main__":
    app = LibraryApp()
    app.run_library()


# testing

#book = Book('Tytuł1', 'Autor1 Aa', '1940')
#book2 = Book('Tytuł B', 'Autor2 Aa', '1945')
#book3 = Book('Tytuł 3C', 'Autor3 Aa', '1960')
#book4 = Book('Tytuł 3C', 'Autor4 dd', '1970')
#print(book)
#book.borrow()
#books = [book,book2]

#library = Library(books)
#print(library)
#library.add_book(book3)
#library.add_book(book4)
#searchResultTitle = library.search_by_title('Tytuł')
#searchResultAuthor = library.search_by_author('Autor')
#library.list_available_books()
#library.borrow_book('Tytuł b')
#library.borrow_book2('Tytuł')

#library.return_book('Tytuł b')
#library.return_book('Tytuł')
